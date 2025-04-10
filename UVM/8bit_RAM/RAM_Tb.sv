/////_____UVM MACROS_____/////
`include "uvm_macros.svh"
import uvm_pkg::*;

/////_____Transaction____/////
// Keep track of all I/O present in DUT (uvm_sequence_item)
class transaction extends uvm_sequence_item;
	`uvm_object_utils(transaction)
	/// Rand input
	rand bit [3:0] addr;
	rand bit clk;
	rand bit wr;
	rand bit [7:0] din;
	/// READ data
	bit [7:0] dout;

	/// To check verification enviroment expected behaviour
	constraint addr_c {addr ==3;}; // Forces addr to be 3
	

	// Constructor
	function new(input string inst = "transaction");
		super.new(inst);
	endfunction


	// No field automation use to implement sformatf
endclass
///________________________________________________________________________
/////_____Sequence_____/////
/// Combination of transactions to verify specific testcases (uvm_sequence)
/// "#(transaction)": parameterized class that works with "transaction"
class generator extends uvm_sequence#(transaction);
	/// Register a simple object with no field automation
	`uvm_object_utils(generator)

	// Instance of transaction
	transaction t;

	// Constructor 
	function new(input string inst = "generator");
		super.new(inst);
	endfunction

	// Main execution block: Its virtual due to polymorphism
	virtual task body();
		for(int i = 0; i < 10; i++)begin
			t = transaction::type_id::create("t");
			start_item(t);
			t.randomize();
			$display("---------------------------------");
			`uvm_info("GEN", $sformatf("SEQ -> Driver wr: %0d, addr: %0d, din: %0d, dout: %0d",t.wr,t.addr,t.din,t.dout),UVM_NONE);
			finish_item(t);
		end 
	endtask
endclass
///________________________________________________________________________
/////_____Driver_____/////
// Send request to driver for sequence, apply sequence to DUT (uvm_driver)
/// "#(transaction)": parameterized class that works with "transaction"
class driver extends uvm_driver#(transaction);
	/// Simple object with no field automation
	`uvm_component_utils(driver)
	
	// Instances: Transaction and DUT
	transaction t;
	virtual ram_if rif;

	/// Constructor
	function new (input string inst = "driver", uvm_component parent = null);
		super.new(inst, parent);
	endfunction
	
	// Build phase
	virtual function void build_phase(uvm_phase phase);
		super.build_phase(phase);
		t = transaction::type_id::create("t");
		if(!uvm_config_db#(virtual ram_if)::get(this,"","rif",rif))
			`uvm_error("DRV","Unable to access Interface");
	endfunction

	// Main phase
	virtual task run_phase(uvm_phase phase);
		forever begin
			// Fetches the next transaction for UVM TLM(Transaction LEvel modeling)
			seq_item_port.get_next_item(t);
			rif.wr <= t.wr;
			rif.din <= t.din;
			rif.addr <= t.addr;
			`uvm_info("DRV", $sformatf("DRV -> DUT wr: %0d, addr: %0d, din: %0d, dout: %0d",t.wr,t.addr,t.din,t.dout),UVM_NONE);
			seq_item_port.item_done();
			// CLK generator
			@(posedge rif.clk);
			// Read enable
			if(t.wr == 1'b0)
				// If is read, wait for a clk cyle before proceeding
				// to allow DUT respond with dout
				@(posedge rif.clk);
	
		end
	endtask
endclass
///________________________________________________________________________
/////_____Monitor_____/////
// Collects response from the DUTand forward to scoreboard (uvm_monitor)
class monitor extends uvm_monitor;
	/// Simple object 
	`uvm_component_utils(monitor)
	// Port that carries transactions
	uvm_analysis_port #(transaction) send;
	
	// Instance of a transaction and DUT 
	virtual ram_if rif;
	transaction t;
	
	// Constructor
	function new(input string inst = "monitor",uvm_component parent = null);
		super.new(inst, parent);
	endfunction

	// Build phase
	virtual function void build_phase(uvm_phase phase);
		super.build_phase(phase);
		t = transaction::type_id::create("t");
		send = new("send",this);
		if(!uvm_config_db#(virtual ram_if)::get(this,"","rif",rif))
			`uvm_error("MON","Unable to access Interface");
	endfunction
	
	// RUN phase
	virtual task run_phase(uvm_phase phase);
		forever begin 
			@(posedge rif.clk);
			t.wr = rif.wr;	
			t.din = rif.din;
			t.addr = rif.addr;
			
			if(rif.wr == 1'b0) begin
				@(posedge rif.clk);
				t.dout = rif.dout;
			end
			
			`uvm_info("DRV", $sformatf("DUT -> MON wr: %0d, addr: %0d, din: %0d,dout: %0d",t.wr,t.addr,t.din,t.dout), UVM_NONE);
			send.write(t);
			end	
	endtask
endclass
///________________________________________________________________________
/////_____Scoreboard_____/////
/// Compare response with golden data (uvm_scoreboard)
class scoreboard extends uvm_scoreboard;
	// UVM Factory: Register a simple object
	`uvm_component_utils(scoreboard)
	// UVM Analysis import port (port)
	uvm_analysis_imp #(transaction,scoreboard) recv; 
	
	// Register of 8 bits, every space is 20 space array
	reg [7:0] tarr[20] = '{default:0};
	
	// Constructor 
	function new(input string inst = "SCO", uvm_component c);
		super.new(inst, c);
		recv = new("recv",this);
	endfunction 
	
	virtual function void write(transaction data);
		if(data.wr == 1'b1)
			begin
				tarr[data.addr] = data.din;
				`uvm_info("SCO", $sformatf("MON -> SCO: DATA WRITE OP: addr: %0d, din: %0d",data.addr,data.din),UVM_NONE);
			end
		else if(data.wr == 1'b0)
			begin 
				if(data.dout == tarr[data.addr])
					begin
					`uvm_info("SCO", $sformatf("TEST PASSED: DATA READ OP addr: %0d,din: %0d, dout: %0d",data.addr,data.din,data.dout),UVM_NONE);
					end
				else 
					begin
					`uvm_error("SCO", $sformatf("TEST FAILED: DATA READ OP addr: %0d, din: %0d, dout: %0d",data.addr,data.din,data.dout));
					end
			end
			$display("----------------------------------------");
	endfunction
endclass
///________________________________________________________________________
/////_____Agent_____/////
/// Encapsulate Driver, sequencer, monitor. Connection of driver, sequencer and TLM port (uvm_agent)
class agent extends uvm_agent;	
	// UVM Factory: Register a simple object
	`uvm_component_utils(agent)
	// Constructor 
	function new(input string inst = "agent",uvm_component parent = null);
		super.new(inst,parent);
	endfunction 
	
	// Instance of monitor, driver and uvm_sequencer
	monitor m;
	driver d;
	uvm_sequencer #(transaction) seqr;	
	
	// Build phase
	virtual function void build_phase(uvm_phase phase);
		super.build_phase(phase);
		m = monitor::type_id::create("m",this);
		d = driver::type_id::create("d",this);
		seqr = uvm_sequencer #(transaction)::type_id::create("seqr",this);
	endfunction

	// Connect phase 
	virtual function void connect_phase(uvm_phase phase);
		super.connect_phase(phase);
		d.seq_item_port.connect(seqr.seq_item_export);
	endfunction
endclass
///________________________________________________________________________
/////_____Enviroment_____/////
/// Encapsulate agent and scoreboard. Connection of analysis port of MONITOR, SCOREBOARD (uvm_enviroment)
class env extends uvm_env;
	// UVM Factory: Register simple object with no field automation
	`uvm_component_utils(env)
	// Constructor
	function new(input string inst = "env", uvm_component parent = null);
		super.new(inst,parent);
	endfunction
	// Instance scoreboard and agent
	scoreboard s;
	agent a;
	
	// Build phase
	virtual function void build_phase(uvm_phase phase);
		super.build_phase(phase);
		a = agent::type_id::create("a",this);
		s = scoreboard::type_id::create("s",this);
	endfunction 

	// Connect phase
	virtual function void connect_phase(uvm_phase phase);
		super.connect_phase(phase);
		a.m.send.connect(s.recv);
	endfunction
endclass
///________________________________________________________________________
/////_____Test_____/////
/// Encapsulate agent and scoreboard. Connection of analysis port of MON,SCO(uvm_test)
class test extends uvm_test;
	// UVM Factory: Register a simple object.
	`uvm_component_utils(test)
	
	// Constructor
	function new(input string inst = "test", uvm_component parent = null);
		super.new(inst,parent);
	endfunction
		
	// Instance of a generator
	generator gen;
	env e;
	
	// Build phase
	virtual function void build_phase(uvm_phase phase);
  		super.build_phase(phase);
    		e = env::type_id::create("e",this);
    		gen = generator::type_id::create("gen",this);
  	endfunction
	
	// Run phase
	virtual task run_phase(uvm_phase phase);
  		phase.raise_objection(this);
  		gen.start(e.a.seqr);
  		#20;  
  		phase.drop_objection(this);
  	endtask

endclass
///________________________________________________________________________
/////_____TB TOP_____/////	

module ram_tb;

	// Instance
	ram_if rif();
	// DUT connection
	ram dut (.clk(rif.clk),.wr(rif.wr),.din(rif.din),.dout(rif.dout),.addr(rif.addr));
	

	// Initial clk
	initial begin 
		rif.clk = 0;
	end
	
	always#10 rif.clk = ~rif.clk;

	initial begin 
		uvm_config_db #(virtual ram_if)::set(null, "*","rif",rif);
		run_test("test");
	end
endmodule