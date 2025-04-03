`include "uvm_macros.svh"
import uvm_pkg::*;
     
     
class drv extends uvm_driver;
	`uvm_component_utils(drv)
     
      	virtual adder_if aif;
     
      	function new(input string path = "drv", uvm_component parent = null);
        	super.new(path,parent);
      	endfunction
     
      	virtual function void build_phase(uvm_phase phase);
      		super.build_phase(phase);
        
        	if(!uvm_config_db#(virtual adder_if)::get(this,"","aif",aif))//drv.aif
          	`uvm_error("drv","Unable to access Interface");
        
      		endfunction
      
       	virtual task run_phase(uvm_phase phase);
         	phase.raise_objection(this);
         	for(int i = 0; i< 10; i++)
          		begin
            			aif.a <= $urandom;
            			aif.b <= $urandom;
            			#10;
          		end
         	phase.drop_objection(this);
       		endtask
     
endclass
     
     
     
     
     
    ////////////////////////////////////////////////////////////////////
module tb;
     
	// Instance object
      	adder_if aif();
      
	// Connect instance to module of adder
      	adder dut (.a(aif.a), .b(aif.b), .y(aif.y));
      
     
	initial 
      		begin
        	uvm_config_db #(virtual adder_if)::set(null, "uvm_test_top", "aif", aif);//uvm_test_top.aif
        
        	run_test("drv"); 
      	end
     
      	initial begin
        	$dumpfile("dump.vcd");
        	$dumpvars;
      	end
endmodule

