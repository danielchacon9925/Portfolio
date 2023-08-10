#Variables
CFLAGS=-Wall
all:
	iverilog -o a.out testbench.v 
	vvp a.out
	gtkwave testMDIO.vcd
	yosys -s  yosys.ys  
