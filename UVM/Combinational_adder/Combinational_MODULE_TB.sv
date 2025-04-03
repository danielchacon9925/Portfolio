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
		super.new(path;
	endfunction

/// Macros for field automation: print, copying, comparing
`uvm_objects_utils_begin(transaction)
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
				`uvm_info("GEN", $sformatf("Data send to driver a: %0d, b: %0d", t.a,t.b),UVM_NONE);
				/// Send to the driver
				finish_item(t); 
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
			`uvm_info("DRV", $sformatf("Trigger DUT a: %0d, b: %0d",data.a,data.b),UVM_NONE);
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
	function new(input string inst = "monitor", uvm_component parent = null);
		super.new(path, parent);
		send = new("send", this);
	endfunction

	/// Instance transaction and DUT
	transaction t;
	virtual add_if aif;

	/// Build phase
	virtual function void build_phase(uvm_phase phase);
		super.build_phase(phase);
		t = transaction::type_id::create("TRANS");
			if(!uvm_config_db #(virtual add_if)::get(this, "","aif",aif))
				`uvm_info("MON", "Unable to access uvm_config_db", UVM_NONE);
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

