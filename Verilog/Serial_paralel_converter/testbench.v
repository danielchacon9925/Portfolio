`include "convertidor_sp_ps.v"
`include "tester.v"

// Se define un modulo para el banco de pruebas

module testbench;

// Las senales se definen como cables
wire CLK, RESET, S_IN, S_START, P_VALID, S_OUT;
wire [31:0] P_OUT, P_IN; 

// Se ctrea una instancia del convertidor

convertidor convertidorINST(
    .CLK      (CLK),
    .RESET    (RESET),
    .S_IN     (S_IN),
    .P_IN     (P_IN),
    .S_START  (S_START),
    .P_VALID  (P_VALID),
    .P_OUT    (P_OUT),
    .S_OUT    (S_OUT)    
);

// Se crea una instancia del probador

Probador probadorINST(
    .CLK      (CLK),
    .RESET    (RESET),
    .S_IN     (S_IN),
    .P_IN     (P_IN),
    .S_START  (S_START),
    .P_VALID  (P_VALID),
    .P_OUT    (P_OUT),
    .S_OUT    (S_OUT)    
);

// Se genera el display para cuando se corra el comando vvp y el archivo .vcd para GTKWave
initial begin
    $dumpfile ("convertidorspps.vcd");
    $dumpvars;
    $display("\t\t\tCLK\| RESET| S_IN |     \tP_OUT                            | P_VALID|S_START|     P_IN                             | S_OUT");
    $display("\t\t\t---------------------------------------------------------------------------------------------------------------------------");
    $monitor( $time, "|\t%b |\t%b |\t%b |\t%b |\t%b |\t%b |\t%b |\t%b", CLK, RESET, S_IN, P_OUT, P_VALID, S_START, P_IN, S_OUT);
    end
    endmodule
