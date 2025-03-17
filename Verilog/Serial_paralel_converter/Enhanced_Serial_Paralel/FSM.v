// TO start the serial to paralel is necesary a code: 0x5A
module FSM(
    input CLK,
    input S_IN,
    input RESET,
    output reg CONVERTION
);

// FSM states
reg [7:0] state;
reg [7:0] nxt_state;           


// 0x5A:01011010

always @(posedge CLK ) begin
    if (RESET) begin
        // Inicia en IDLE
        state <= 8'b00000001;
        case(state)
            8'b00000001: if (S_IN) begin
                nxt_state = 8'b00000001;
                CONVERTION = 1'b0;
            end else begin
                nxt_state = 8'b00000010;
                CONVERTION = 1'b0;
            end
            8'b00000010: if (S_IN) begin
                nxt_state = 8'b00000101;
                CONVERTION = 1'b0;
            end else begin
                nxt_state = 8'b00000010;
                CONVERTION = 1'b0;               
            end
            8'b00000101: if (S_IN) begin
                nxt_state = 8'b00001011;
                CONVERTION = 1'b0;
            end else begin
                nxt_state = 8'b00000101;
                CONVERTION = 1'b0;
            end
            8'b00001011: if (S_IN) begin
                nxt_state = 8'b00001011;
                CONVERTION = 1'b0;
            end else begin
                nxt_state = 8'b00010110;
                CONVERTION = 1'b0;                
            end
            8'b00010110: if (S_IN) begin
                nxt_state = 8'b00101101;
                CONVERTION = 1'b0;
            end else begin
                nxt_state = 8'b00010110;
                CONVERTION = 1'b0;                
            end
            8'b00101101: if (S_IN) begin
                nxt_state = 8'b00101101;
                CONVERTION = 1'b0;
            end else begin
                nxt_state = 8'b01011010;
                CONVERTION = 1'b0;                
            end
            8'b01011010: begin
                // Caracter de entrada recibido
                CONVERTION = 1'b1;
            end
            default:   nxt_state = 8'b00000001;
        endcase
    end else begin
        state <= nxt_state;
    end
end


endmodule