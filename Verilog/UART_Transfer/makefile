# Variables
CFLAGS=-Wall
all:
		iverilog -o rx_out_test.out RX_Tb.v
		vvp rx_out_test.out
		gtkwave test_RX_UART.vcd