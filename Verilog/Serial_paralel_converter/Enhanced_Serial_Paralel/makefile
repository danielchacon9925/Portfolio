CFLAGS=-Wall
all:
	iverilog -o test.out TESTBENCH.v
	vvp test.out
	gtkwave seriestoparalel.vcd