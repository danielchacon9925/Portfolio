`include "registrofinal.v"
module DUT(S_OUT, clk, ENB, DIR, S_IN, MODO, D, Q);
	
// Input/Output definition
input wire clk;
input wire ENB;
input wire DIR;
input wire S_IN;
input wire [1:0] MODO;
input wire [3:0] D;
output wire [3:0] Q;
output wire S_OUT;

registrodesplazable inst1(
    .S_OUT  (S_OUT),
    .clk    (clk),
    .ENB    (ENB),
    .DIR    (DIR),
    .S_IN   (S_IN),
    .MODO   (MODO),
    .D      (D),
    .Q      (Q)
);

endmodule