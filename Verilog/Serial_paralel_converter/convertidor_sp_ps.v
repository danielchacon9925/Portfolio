`include "serieaparalelo.v"
`include "paraleloaserie.v"

module convertidor (CLK, RESET, S_IN, P_IN, S_START, P_VALID, P_OUT, S_OUT);

// Se definen las entradas del modulo
input CLK, RESET, S_IN, S_START; 
input [31:0] P_IN ;

// Se definen las salidas del modulo
output wire P_VALID, S_OUT;
output wire [31:0] P_OUT;  

// Se instancia el modulo que convierte de serie a paralelo
serieaparalelo SP(
    .CLK      (CLK),
    .RESET    (RESET),
    .S_IN     (S_IN),
    .P_OUT    (P_OUT),
    .P_VALID  (P_VALID)
);

// Se instancia el modulo que convierte de paralelo a serie
paraleloaserie PS(
    .CLK      (CLK),
    .RESET    (RESET),
    .P_IN     (P_IN),
    .S_START  (S_START),
    .S_OUT    (S_OUT)
);

endmodule
