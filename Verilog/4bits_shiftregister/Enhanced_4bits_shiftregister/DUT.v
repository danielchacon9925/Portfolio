`include "4bits_shiftregister.v"

module DUT(
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
    output wire [3:0] Q,
    // Serial output
    output wire S_OUT
);

register Tested_circuit(
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