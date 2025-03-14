module UART(
    input clk, reset, rx, rd_uart, wr_uart,
    input [7:0] w_data,
    input [31:0] dvsr,
    output tx, rx_empty, tx_full,
    output [7:0] r_data,
    output full, almostempty1, almostempty2,
    output wr_ack1, wr_ack2, overflow1, overflow2,
    output underflow1, underflow2, almostfull1, almostfull1
);

endmodule