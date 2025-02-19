// ANSI-C Style Module Definition Verilog 2001+

module baud_rate_generator(
    input clk,
    input reset,
    input [31:0] dvsr,
    output reg tick 
);

// NOn ANSI-C Style Module Definition Verilog 1995
//module baud_rate_generator(clk,reset,dvsr,tick);
//    input clk,
//    input reset,
//    input [31:0] dvsr,
//    output reg tick 

// Internal register
reg [31:0] count;

// Always block: triggered on the rising edge of the clk or reset
always @(posedge clk or posedge reset) begin

    // Reset
    if (reset) begin
        count <= 0;
        tick <= 0;
    end

    
    else begin 
        if (count == dvsr) begin
            count <= 0;
            // Pulse transition: 0 to 1 
            tick <= ~tick;
        end
        else begin
            count <= count +1;
        end

    end
end
endmodule