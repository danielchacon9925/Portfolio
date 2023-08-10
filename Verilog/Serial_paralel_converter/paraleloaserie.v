module paraleloaserie (CLK, RESET, P_IN, S_START, S_OUT);

// Se definen las entradas del modulo
input  CLK, RESET, S_START;
input [31:0] P_IN;

// Se define la salida del modulo
output reg S_OUT; 

// Se define un contador para los ciclos
integer cont = 32;

// Se define el ciclo principal
always @(posedge CLK) begin
    // si reset es 1
    if (RESET == 1'b1) begin

        // Si S_START = 1 , cargar un bit de p_in en s_out
        if (S_START == 1'b1) begin
            S_OUT <= P_IN[cont]; 
            cont <=  cont - 1; 
           
        end
        // Para cualquier otro caso
        else if ((S_START == 1'b0)) begin
            S_OUT <= S_OUT;
        end
    end

    // Si reset es 0. todas las salidas son 0
    else if(RESET == 0)begin
        S_OUT <= 0;
    end
end
endmodule
