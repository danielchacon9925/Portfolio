module paraleltoseries(
    input CLK,
    input RESET,
    input S_START,
    input [31:0] P_IN,
    output reg S_OUT
);

// Counter to add S_OUT=P_IN[count]
integer cont = 31;

always @(posedge CLK) begin
    if (RESET) begin
        if (S_START) begin 
            // Serial out
            S_OUT <= P_IN[cont];
            // Update counter
            cont <= cont - 1;
        end else begin
            S_OUT <= S_OUT;
        end
    end else begin
        // 0 out
        S_OUT <= 0;
    end
end
endmodule