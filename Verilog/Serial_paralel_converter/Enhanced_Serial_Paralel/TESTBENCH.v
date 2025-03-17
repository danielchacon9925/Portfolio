`include "SERIES_PARALEL_Converter.v"
`include "TESTER.v"

module testbench;

wire CLK;
wire RESET;
wire S_START;
wire S_IN;
wire [31:0] P_IN;
wire P_VALID;
wire S_OUT;
wire [31:0] P_OUT;

CONVERTER CONVERTER1(
    .CLK(CLK),
    .RESET(RESET),
    .S_START(S_START),
    .S_IN(S_IN),
    .P_IN(P_IN),
    .P_VALID(P_VALID),
    .S_OUT(S_OUT),
    .P_OUT(P_OUT)
);

TESTER TESTER1(
    .CLK(CLK),
    .RESET(RESET),
    .S_START(S_START),
    .S_IN(S_IN),
    .P_IN(P_IN),
    .P_VALID(P_VALID),
    .S_OUT(S_OUT),
    .P_OUT(P_OUT)
);
endmodule