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