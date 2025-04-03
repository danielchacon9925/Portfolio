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

/// Macros for print, copying, comparing
`uvm_objects_utils_begin(transaction)
`uvm_field_int(a, UVM_DEFAULT)
`uvm_field_int(b, UVM_DEFAULT)
`uvm_field_int(y, UVM_DEFAULT)
`uvm_object_utils_end
endclass
