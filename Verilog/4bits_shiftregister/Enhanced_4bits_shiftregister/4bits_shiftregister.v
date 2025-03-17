module register(
    // CLK
    input CLK,
    // Transactions enabled
    input ENB,
    // Direction for the rotation
    input DIR,
    // Serial entry
    input S_IN,
    // MODE 
    input [1:0] MODO,
    // Paralel entry
    input [3:0] D,
    // Paralel output
    output reg [3:0] Q,
    // Serial output
    output reg S_OUT
);
// Params for FSM
localparam SHIFT = 2'b00;
localparam CIRCULAR_SHIFT = 2'b01;
localparam PARALEL = 2'b10;
localparam RESET = 2'b11;
// Using cases to compare results
always @(posedge CLK) begin
    if (!ENB) begin
        // IDLE
        Q <= Q;
        S_OUT <= S_OUT;
    end else begin
        case(MODO)
            // Shift
            SHIFT: begin
                if (!DIR) begin
                    // Left
                    S_OUT <= Q[3];
                    Q <= {Q[2:0], S_IN};
                end else begin
                    // Right
                    S_OUT <= Q[0];
                    Q <= {S_IN, Q[3:1]};                   
                end
            end
            // Circular Shift
            CIRCULAR_SHIFT: begin
                if (!DIR) begin
                    // Left
                    Q[3:0] <= {Q[2:0], Q[3]};
                    S_OUT <= 1'b0;
                end else begin
                    // Right
                    Q[3:0] <= {Q[0], Q[3:1]};
                    S_OUT <= 1'b0;
                end
            end
            // Paralel load
            PARALEL: begin
                Q[3:0] <= D[3:0];
                S_OUT <= 1'b0;
            end
            // RESET
            RESET: begin
                S_OUT <= 1'b0;
            end
            // Default IDLE
            default: begin
                // IDLE
                Q <= Q;
                S_OUT <= S_OUT;               
            end
        endcase
    end
end

endmodule




