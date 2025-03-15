`include "FIFO.v"
`include "RX.v"
`include "baud_rate_generator.v"

module rx_tb;
    reg clk;
    reg reset;
    reg [31:0] dvsr;
    wire tick;
    reg rx;
    wire [7:0] dout;
    wire rx_done_tick;
    logic rd_uart;
    wire [7:0] r_data;

    // Baud rate generator
    baud_rate_generator baud_gen(
        .clk(clk),
        .reset(reset),
        .dvsr(dvsr),
        .tick(tick)
    );
    // UART RX
    rx u_rx(
        .s_tick(tick),
        .clk(clk),
        .reset(reset),
        .rx(rx),
        .dout(dout),
        .rx_done_tick(rx_done_tick)
    );
    // FIFO 
    FIFO fifo(
        .data_in(dout),
        .wr_en(rx_done_tick),
        .rd_en(rd_uart),
        .clk(clk),
        .rst_n(~reset),
        .full(full),
        .empty(empty),
        .data_out(r_data)
    );

    initial begin
        clk = 0;
        forever #5 clk = ~clk;
    end

    // Apply reset
    initial begin
        reset = 1;
        #20 reset = 0;
    end

    initial begin
        dvsr = 0;
        rx = 1;
        rd_uart = 0;

        // Dump waveform data
        $dumpfile("test_RX_UART.vcd");
        // Dump all signs from testbench
        $dumpvars(0, rx_tb);
        // Wait reset to complete
        #30;

        // Send start bit (0)
        rx = 0;
        #320; // WAit for 1 bit duration 16*540ns

        // Send data bits (LSB first: 1,0,1,0,0,1,0,1)
        rx = 1; // bit 0
        #320;
        rx = 0; // bit 1
        #320;
        rx = 1; // bit 2
        #320;
        rx = 0; // bit 3
        #320;
        rx = 0; // bit 4
        #320;
        rx = 1; // bit 5
        #320;
        rx = 0; // bit 6
        #320;
        rx = 1; // bit 7
        #320;

        // send stop bit (1)
        rx = 1;
        #320;

        rd_uart = 1;
        #320;
        $display("Received data: 0x%h", r_data);
        if (dout == 8'hA5)
            $display("Test Passed!");
        else 
            $display("Test failed!");
        $finish;
    end
endmodule