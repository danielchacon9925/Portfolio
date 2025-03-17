#Variables
CFLAGS=-Wall
all:
	iverilog -o test.out TESTBENCH.v 
	vvp test.out
	gtkwave Test_4bits_shiftregister.vcd