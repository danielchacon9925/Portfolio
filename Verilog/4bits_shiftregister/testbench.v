//`include "registrofinal.v"
`include "tester.v"
`include "DUT.v"
// Se define un modulo para el banco de pruebas

module testbench;

// Las senales se definen como cables
wire clk, ENB, DIR, S_IN;
wire S_OUT;
wire  [3:0] Q;
wire  [3:0] D; 
wire [1:0] MODO;

// Se crea instancia del probador

DUT Shiftregister(
    .S_OUT  (S_OUT),
    .clk    (clk),
    .ENB    (ENB),
    .DIR    (DIR),
    .S_IN   (S_IN),
    .MODO   (MODO),
    .D      (D),
    .Q      (Q)
);

Probador Tester(
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

