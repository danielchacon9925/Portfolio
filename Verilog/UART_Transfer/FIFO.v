// Non-ANSI Style JUST IN CASE
//module FIFO (data_in, clk, rst_n, wr_en, rd_en, data_out, wr_ack, overflow, underflow, full, empty, almostfull, almostempty);

    // Parameter declarations
//    parameter FIFO_WIDTH = 8;
//    parameter FIFO_DEPTH = 8;

    // Input port declarations
//    input [FIFO_WIDTH-1:0] data_in;
//    input clk, rst_n, wr_en, rd_en;

    // Output port declarations
//    output [FIFO_WIDTH-1:0] data_out;
//    output wr_ack, overflow, underflow;
//    output full, empty, almostfull, almostempty;

    // Register declarations for outputs
//    reg [FIFO_WIDTH-1:0] data_out;
//    reg wr_ack, overflow, underflow;

    // FIFO logic goes here

//endmodule


module FIFO #(
    parameter FIFO_WIDTH = 8,
    parameter FIFO_DEPTH = 8
)(
    // [N-1:0] range of bits. Verilog uses zero-based indexing
    input [FIFO_WIDTH-1:0] data_in,
    input clk, rst_n, wr_en, rd_en,
    output reg [FIFO_WIDTH-1:0] data_out,
    output reg wr_ack, overflow, underflow,
    output full, empty, almostfull, almostempty
);

// Minimun number of bits required to represent the input number in binary
localparam  max_fifo_addr = $clog2(FIFO_DEPTH-1:0);

// MEM array with FIFO_DEPTH and FIFO_WIDTH on each entry of memory
reg [FIFO_WIDTH-1:0] mem [FIFO_DEPTH-1:0];

// Pointers to track the read and write locations
reg [max_fifo_addr-1:0] wr_ptr, rd_ptr;
reg [max_fifo_addr:0] count; 

always @(posedge clk or posedge rst_n) begin
    // reset
    if (!rst_n) begin
        wr_ptr <= 0;
        wr_ack <=0;
        overflow <= 0;
    end
    else if (wr_en && count < FIFO_DEPTH) begin
        // Data written where pointer indicates
        mem[wr_ptr] <= data_in;
        wr_ack <= 1;
        // Pointer incremented
        wr_ptr <= wr_ptr + 1;
    end
    else if ({wr_en,rd_en} == 2'b00) begin 
    // IDLE state
    end
    // DEFAULT STATE (No write or overwrite)
    else begin
        wr_ack <= 0;
        // FIFO Full and not for reading
        if (full && wr_en && !rd_en) begin
            // Overflow
            overflow <= 1;
        end
        else begin
            overflow <= 0;
        end
    end
// End Always Blocking Posedge
end

always @(posedge clk or negedge rst_n) begin
    // reset
    if (!rst_n) begin 
        rd_prt <= 0;
        underflow <= 0;
    end
    else if (rd_en && count != 0) begin
        // Data read where pointer indicates
        data_out <= mem[rd_ptr];
        // Pointer incremented
        rd_ptr <= rd_ptr + 1;
    end
    else if ({wr_en, rd_en} == 2'b00) begin
        // IDLE STATE
    end
    // Default STATE (no read or overwrite)
    else begin

        if (rd_en && !wr_en && empty) begin
            underflow <= 1;
        end
        else begin
            underflow <= 0;
        end
    end
end

always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        count <= 0;
    end
    else begin
        // Write operation
        if (({wr_en, rd_en} == 2'b10) && !full)
            count <= count + 1;
        // Read operation
        else if (({wr_en, rd_en} == 2'b01) && !empty)
            count <= count - 1;
        else if (({wr_en, rd_en} == 2'b11) && !full) begin
            count <= count - 1;
        end
        else if (({wr_en, rd_en} == 2'b11) && !empty) begin
            count <= count - 1;
        end
        else begin
            // IDLE State
        end            
    end
end

// Combinational logic 
assign full = (count == FIFO_DEPTH)? 1: 0;
assing empty = (count == 0)? 1 : 0;
assign almostfull = (count == FIFO_DEPTH-1)? 1 : 0;
assign almostempty = (count == 1)? 1 : 0;

// Endmodule
endmodule