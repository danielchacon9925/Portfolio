`include "seriestoparalel.v"
`include "paraleltoseries.v"

module CONVERTER(
    input CLK, 
    input RESET, 
    input S_START, 
    input S_IN,
    input [31:0] P_IN,
    output wire P_VALID, S_OUT,
    output wire [31:0] P_OUT
);

// Instance

seriestoparalel SP(
    .CLK (CLK),
    .RESET (RESET),
    .S_IN (S_IN),
    .P_VALID (P_VALID),
    .P_OUT (P_OUT)
);

paraleltoseries PS(
    .CLK (CLK),
    .RESET (RESET),
    .S_START (S_START),
    .P_IN (P_IN),
    .S_OUT (S_OUT)
);

endmodule