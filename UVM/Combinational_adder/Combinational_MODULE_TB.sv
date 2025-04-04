/////_____Testbench_time_scale_____/////
`timescale 1ns / 1ps

////_____UVM_Macros_____/////
`include "uvm_macros.svh"
import uvm_pkg::*;

/////_____Transaction_____/////
/// Keep track of all I/O present in DUT (uvm_sequence_item)
class transaction extends uvm_sequence_item;
	/// I/O
	rand bit [3:0] a;
	rand bit [3:0] b;
	bit [4:0] y;
	/// Constructor
	function new(input string path = "transaction");
		super.new(path);
	endfunction

/// Macros for field automation: print, copying, comparing
`uvm_object_utils_begin(transaction)
`uvm_field_int(a, UVM_DEFAULT)
`uvm_field_int(b, UVM_DEFAULT)
`uvm_field_int(y, UVM_DEFAULT)
`uvm_object_utils_end

endclass
///________________________________________________________________________
/////_____Sequence_____/////
/// Combination of transactions to verify specific testcases (uvm_sequence)
/// "#(transaction)": parameterized class that works with "transaction"
class generator extends uvm_sequence #(transaction);
	/// Register a simple object with no field automation
	`uvm_object_utils(generator)

	///// Instance transaction class
	/// Used because of start and finish item
	transaction t;
	/// Counter for stimuli
	integer i;
	/// Constructor
	function new(input string path = "generator");
		super.new(path);
	endfunction
	/// Main execution block: Its virtual due to polymorphism
	/// Child classes can redifine body without modifying base class
	virtual task body();
		t = transaction::type_id::create("t");
		repeat(10)
			begin
				/// Request access the driver
				start_item(t);
				/// Random number generator
				t.randomize();
				/// UVM reporting macros
				`uvm_info("GEN", $sformatf("Data send to driver a: %0d, b: %0d", t.a,t.b), UVM_NONE);
				/// Send to the driver
				finish_item(t); 
			end
	endtask
endclass
///________________________________________________________________________
/////_____Driver_____/////
/// Send request to driver for sequence, apply sequence to the DUT (uvm_driver)
/// "#(transaction)": parameterized class that works with "transaction"	
class driver extends uvm_driver #(transaction);
	/// Register a simple object with no field automation
	`uvm_component_utils(driver)

	///// Instance transaction class
	/// Used because of start and finish item
	transaction tc;
	/// Constructor 
	function new(input string path = "driver", uvm_component parent = null);
		super.new(path, parent);
	endfunction
	/// Interface declaration: Connect to DUT signals.
	virtual add_if aif; 

	/// Build phase
	virtual function void build_phase(uvm_phase phase);
		super.build_phase(phase);
		tc = transaction::type_id::create("tc");
		/// Get configuration database for a virtual interface
		if(!uvm_config_db #(virtual add_if)::get(this,"","aif",aif))
			`uvm_error("DRV", "Unable to access uvm_config_db");
	endfunction
	
	/// Run phase
	virtual task run_phase(uvm_phase phase);
		forever begin
			/// Gets next transaction item from sequencer
			seq_item_port.get_next_item(tc);
			/// Drive transaction data onto interface
			aif.a <= tc.a;
			aif.b <= tc.b;
			`uvm_info("DRV", $sformatf("Trigger DUT a: %0d, b: %0d",tc.a,tc.b),UVM_NONE);
			seq_item_port.item_done();
			#10;
			end
	endtask
endclass
///________________________________________________________________________
/////_____Monitor_____/////
/// Collect response of DUT and forward to scoreboard (UVM_SCOREBOARD)
class monitor extends uvm_monitor;
	/// Register a simple object with no field automation
	`uvm_component_utils(monitor)
	/// Port that carries transactions
	uvm_analysis_port #(transaction) send;
	
	/// Constructor
	function new(input string path = "monitor", uvm_component parent = null);
		super.new(path, parent);
		send = new("send", this);
	endfunction

	/// Instance transaction and DUT
	transaction t;
	virtual add_if aif;

	/// Build phase
	virtual function void build_phase(uvm_phase phase);
		super.build_phase(phase);
		t = transaction::type_id::create("t");
			if(!uvm_config_db #(virtual add_if)::get(this, "","aif",aif))
				`uvm_error("MON", "Unable to access uvm_config_db");
			endfunction
	/// RUN phase
	virtual task run_phase(uvm_phase phase);
		forever begin 
			#10;
			t.a = aif.a;
			t.b = aif.b;
			t.y = aif.y;
			`uvm_info("MON", $sformatf("Data send to Scoreboard a: %0d, b: %0d and y: %0d",t.a,t.b,t.y), UVM_NONE);
			send.write(t);
			end
	endtask
endclass
///________________________________________________________________________
/////_____Scoreboard_____/////
/// Compare response with golden data (uvm_scoreboard)
class scoreboard extends uvm_scoreboard;
	/// UVM Factory: Register a simple object with no field automation
	`uvm_component_utils(scoreboard)
	/// UVM analysis import port (recv) parameterized to accept objects of type transaction
	/// and bound to this scoreboard 
	uvm_analysis_imp #(transaction, scoreboard) recv;

	/// Instance of transaction 
	transaction tr;
	
	/// Constructor 
	function new(input string path = "scoreboard", uvm_component parent = null);
		super.new(path, parent);
		recv = new("Read", this);
	endfunction

	/// Build phase 
	virtual function void build_phase(uvm_phase phase);
		super.build_phase(phase);
		tr = transaction::type_id::create("tr");
	endfunction
	
	/// Write method data to transaction object (local tr) to update
	virtual function void write(input transaction t);
		tr = t;
		`uvm_info("SCO",$sformatf("Data rcvd from monitor a: %0d, b: %0d and y: %0d", tr.a,tr.b,tr.y),UVM_NONE);
	
		if(tr.y == tr.a + tr.b)
			`uvm_info("SCO","Test Passed", UVM_NONE)
		else 
			`uvm_info("SCO","Test Failed", UVM_NONE)
	endfunction
endclass
///________________________________________________________________________
/////_____Agent_____/////
/// Encapsulate driver, sequencer, monitor. Connection of driver, sequencer and TLM Port (uvm_agent)
class agent extends uvm_agent;
	/// UVM Fabric: Simple object with no fiel automation
	`uvm_component_utils(agent)
	/// Constructor
	function new(input string inst = "AGENT", uvm_component c);
		super.new(inst, c);
	endfunction

	/// Instance for classes
	monitor m;
	driver d;
	uvm_sequencer #(transaction) seqr;
	
	/// Build phase
	virtual function void build_phase(uvm_phase phase);
		super.build_phase(phase);
		m = monitor::type_id::create("m", this);
		d = driver::type_id::create("d", this);
		seqr = uvm_sequencer #(transaction)::type_id::create("SEQ", this);
	endfunction

	/// Connect phase
	virtual function void connect_phase(uvm_phase phase);
		super.connect_phase(phase);
		d.seq_item_port.connect(seqr.seq_item_export);
	endfunction
endclass
///________________________________________________________________________
/////_____Enviroment_____/////
/// Encapsulate agent and scoreboard. Connection of analysis port of mon,sco (uvm_env)
class env extends uvm_env;
	/// UVM Factory: Register a simple object with no field automation
	`uvm_component_utils(env)		
	/// Constructor 
	function new(input string inst = "ENV", uvm_component c);
		super.new(inst, c);
	endfunction

	/// Instance of clases
	scoreboard s;
	agent a;

	/// Build phase
	virtual function void build_phase(uvm_phase phase);
		super.build_phase(phase);
		s = scoreboard::type_id::create("s",this);
		a = agent::type_id::create("a",this);
	endfunction
	/// Connect phase
	virtual function void connect_phase(uvm_phase phase);
		super.connect_phase(phase);
		a.m.send.connect(s.recv);
	endfunction
endclass
///________________________________________________________________________
/////_____Test_____/////
/// Encapsulate agent and scoreboard. Connection of analysis port of mon,sco (uvm_env)
class test extends uvm_test;
	/// UVM Factory: Register a simple object with no field automation
	`uvm_component_utils(test)
	
	/// Constructor 
	function new(input string inst = "TEST",uvm_component c);
		super.new(inst,c);
	endfunction
	/// Instance of objects
	generator gen;
	env e;

	/// Build phase
	virtual function void build_phase(uvm_phase phase);
		super.build_phase(phase);
		gen = generator::type_id::create("gen");
		e = env::type_id::create("e",this);
	endfunction

	/// Run phase
	virtual task run_phase(uvm_phase phase);
		phase.raise_objection(this);
		/// Start sequence(in enviroment is agent and in agent is the sequencer)
		gen.start(e.a.seqr);
		#50;
		phase.drop_objection(this);
	endtask
endclass
///________________________________________________________________________
/////_____TB TOP_____/////	

module add_tb();

/// Instance of interface
add_if aif();

/// Instance of module DUT
add dut (.a(aif.a),.b(aif.b),.y(aif.y));

initial begin
	$dumpfile("dump_COMBINATIONAL.vcd");
	$dumpvars;
end

initial begin 
	uvm_config_db #(virtual add_if)::set(null,"uvm_test_top.e.a*","aif",aif);
	run_test("test");
end
endmodule

	