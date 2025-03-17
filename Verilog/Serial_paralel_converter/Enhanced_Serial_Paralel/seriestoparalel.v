`include "FSM.v"
module seriestoparalel(
    input CLK,
    input RESET,
    input S_IN,
    output reg P_VALID,
    output reg [31:0] P_OUT 
); 

// Signal from FSM
wire CONVERTION_ON;
// Counter to validate transaction
integer cont = 31;

FSM maquina(
    .CLK(CLK),
    .S_IN(S_IN),
    .RESET(RESET),
    .CONVERTION(CONVERTION_ON)
);

always @(posedge CLK ) begin
    if (RESET) begin
        if (CONVERTION_ON) begin
            // Full transaction compleated
            if (cont == 0) begin
                P_VALID <= 1;
                P_OUT <= P_OUT;
            end else begin
                P_VALID <= 0;
            end
            //Append to reg
            P_OUT[cont] <= S_IN;
            // Update counter
            cont <= cont - 1;            
        end
    end else begin
        P_OUT <= 32'b0;
        P_VALID <= 1'b0;
    end
end

endmodule