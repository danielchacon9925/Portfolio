`include "DUT.v"
`include "TESTER.v"

module testbench;

// Cables to connect DUT and TESTER
wire CLK, ENB, DIR, S_IN, S_OUT;
wire [1:0] MODO;
wire [3:0] D;
wire [3:0] Q;

DUT DUT1(
    .CLK(CLK),
    .ENB(ENB),
    .DIR(DIR),
    .S_IN(S_IN),
    .MODO(MODO),
    .D(D),
    .Q(Q),
    .S_OUT(S_OUT)  
);

tester TESTER(
    .CLK(CLK),
    .ENB(ENB),
    .DIR(DIR),
    .S_IN(S_IN),
    .MODO(MODO),
    .D(D),
    .Q(Q),
    .S_OUT(S_OUT)
);


endmodule