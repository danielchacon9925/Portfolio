`include "maquina.v"
module serieaparalelo (CLK, RESET, S_IN, P_OUT, P_VALID);
 // Entradas del modulo
    input CLK, RESET, S_IN;

 // Salidas del modulo
    output reg P_VALID;
    output reg [31:0] P_OUT; 

//Conexiones con maquina 

    wire CLK, RESET, S_IN, conver_ON ;

    // Se guarda el indice del registro y el contador respectivamente
    integer cont = 32 ;
    
    // Se instancia la maquina de estados pata obtener el caracter de inicio 0x5A
    maquinadeestados conv (
    .RESET  (RESET),
    .S_IN  (S_IN),
    .CLK    (CLK),
    .conv  (conver_ON));

    // Se define el ciclo principal 
    always @(posedge CLK) begin 

        if (RESET == 1) begin

 // Si se detecta 0x5A en la entrada serial
            if (conver_ON == 1)begin
                // Se asigna a p_out el valor de s_in en el bit correspondiente
                P_OUT[cont] <=  S_IN;
                cont <= cont - 1;

 //Transmisión incompleta de los 32 bits
                if(cont != 0 )begin
                    P_VALID = 1'b0;
                end
            
 //Se activa  P_VALID = 1
                else begin
                P_VALID <= 1'b1;
                end
            end
        end
 //Si se pone RESET = 0, todas las salidas se ponen en 0
        else if (RESET == 0) begin
            P_OUT [31:0] = 32'b0; 
            P_VALID = 1'b0; 
        end
    end
endmodule
