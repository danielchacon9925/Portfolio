module tx(
    // Inputs
    input s_tick, clk, reset, tx_start,
    input [7:0] din,
    // Outputs
    output reg tx,
    output reg tx_done_tick
);


// Localparams 
localparam IDLE = 2'b00;
localparam START = 2'b01;
localparam DATA = 2'b10;
localparam STOP = 2'b11;
// Middle of the bit for 16x Oversampling
localparam MIDBIT = 8;

// Internal registers

reg [1:0] state;
// Oversampling counter: up to 15
reg [3:0] count; 
reg [3:0] bit_count;


// Always block

always @(posedge clk or posedge reset) begin

    // Reset
    if (reset) begin
        // Idle state
        state <= IDLE;
        // Counter restart
        count <= 0;
        // Bit_count
        bit_count <= 0;
        // Signal to stop transmiting
        tx_done_tick <= 0;
        // TX EN
        tx <= 1;
    end

    // Cases
    else begin

        tx_done_tick <= 0; // Default to 0, only until finish is 1.
        // Only at baud rate tick
        if (s_tick) begin

            case (state)
                // IDLE
                IDLE: begin
                    if (!tx_start) begin
                        state <= START;
                        count <= 0;
                        bit_count <= 0;
                    end
                end

                // START
                START: begin
                    if (count == MIDBIT - 1) begin
                        if (!tx_start) begin
                            state <= DATA;
                            count <= 0;
                            tx <= 0;                           
                        end 
                        else begin // False start
                            state <= IDLE;
                        end
                    end
                    else begin
                        state <= IDLE;
                    end
                end
                    else begin
                        count <= count + 1;
                    end

                // DATA
                DATA: begin
                    if (count == 15) begin // Wait 16 ticks per bit
                        tx <= din[bit_count]; // Capture bit (LSB First)
                        count <= 0;
                        if (bit_count == 8) begin
                            state <= STOP;
                            tx <= 1;
                            count <= 0;                           
                        end 
                        else begin // False start
                            bit_count <= bit_count + 1;
                        end
                    end
                    else begin
                        count <= count + 1;
                    end
                end

                // STOP
                STOP: begin
                    if (count == 15) begin
                        if (!tx_start) begin
                            state <= IDLE;
                            tx_done_tick <= 1;
                        end 
                        else begin // False start
                            count <= count + 1;
                        end
                    end
                end

            endcase
        end
    end
end


endmodule