module add(
	input [3:0] a,
	input [3:0] b,
	output [4:0] y
);

assign y = a + b;

endmodule

/////////////////___INTERFACE___/////////////////
/// UVM/System Verilog is OOP/ Dynamic, Verilog is static 
/// The interface acts as bundle of wires connecting between them

interface add_if();

logic [3:0] a;
logic [3:0] b;
logic [4:0] y;

endinterface
