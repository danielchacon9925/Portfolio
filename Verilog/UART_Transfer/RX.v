module rx(
    input s_tick, clk, reset, rx, 
    output reg [7:0] dout,
    output reg rx_done_tick
);

// Params for FSM 
localparam IDLE = 2'b00;
localparam START = 2'b01;
localparam DATA = 2'b10;
localparam STOP = 2'b11;
localparam MIDBIT = 8; // Middle of the bit for oversampling 

reg [1:0] state;
reg [7:0] data_reg;
reg [3:0] count; // Counts up to 15 for 16x oversampling
reg [2:0] bit_count;

// Always block
always @(posedge clk or posedge reset) begin
    // Reset state
    if (reset) begin
        state <= IDLE;
        count <= 0;
        bit_count <= 0;
        rx_done_tick <= 0;
        dout <= 8'b0;
        data_reg <= 8'b0;
    end else begin 
        rx_done_tick <= 0; // Default to 0, pulse only when done
        if (s_tick) begin 
            case(state)

                IDLE: begin
                    if (!rx) begin
                        state <= START;
                        count <= 0;
                        bit_count <= 0;
                    end
                end

                START: begin 
                    if (count == MIDBIT - 1) begin 
                        if  (!rx) begin
                            state <= DATA; 
                            count <= 0;
                        end else begin
                            state <= IDLE;
                        end
                    end else begin 
                        count <= count + 1;
                    end
                end


                DATA: begin 
                    if (count == 15) begin  // Wait 16 ticks per bit
                        data_reg[bit_count] <= rx;  // Capture bit (LSB first)
                        count <= 0;
                        if (bit_count == 7) begin
                            state <= STOP;
                        end else begin
                            bit_count <= bit_count + 1;
                        end

                    end else begin
                        count <= count + 1;
                    end
                end

                STOP: begin
                    if (count == 15) begin  // Wait for stop bit duration
                        state <= IDLE;
                        dout <= data_reg;
                        rx_done_tick <= 1; // Pulse done signal
                    end else begin 
                        count <= count + 1;
                    end
                end
            
            //End cases
            endcase
        end
    // End FSM
    end
// Always block end
end 

endmodule