module maquinadeestados (CLK, RESET, S_IN, conv);

// Definicion de entradas y salidas
input CLK, RESET, S_IN;
output reg conv;

// Registros donde se guardan los valores de lso estados actual y siguiente
reg [7:0] state;
reg [7:0] nxt_state;           

// Definicion de FF                 
always @(posedge CLK) begin
  if (~RESET) begin
    // Estado IDLE
    state  <= 8'b00000001;
    conv = 1'b0;
  end else begin
 // Definición de lo que pasa en las salidas
    state  <= nxt_state;
    conv <= 1'b1;
  end
end

// Logica combinacional - Estados
always @(*) begin

// Comportamiento de la maquina de estados
// Define las transiciones de proximo estado

  case(state)
    8'b00000001: if (S_IN) begin         // Si S_IN=1 se pasa al siguiente estado 
                  nxt_state = 8'b00000010;
                  conv = 1'b0;
                end
                         
    8'b00000010: begin			// Si S_IN=0 se pasa al siguiente estado
                 if (~S_IN) begin 
                  nxt_state = 8'b00000100; 
                  conv = 1'b0;  
                 end
                 else nxt_state = 8'b00000010;	// Si S_IN=1 nos quedamos en este codigo                                                        
                 end

    8'b00000100: begin			// Cuando S_IN=1 se pasa al siguiente estado 
                 if (S_IN) begin
                  nxt_state = 8'b00001000;
                  conv = 1'b0;
                 end   
                 else nxt_state = 8'b00000001; // Cuando S_IN=0 se devuelve al IDLE
                 end 
           
    8'b00001000: begin			//Se pasa al siguiente estado con S_IN=1                     
                 if (S_IN) begin
                  nxt_state = 8'b00010000;
                  conv = 1'b0;
                 end
                 else nxt_state = 8'b00000100; //Se devuelve al estado anterior
               end
               
    8'b00010000: begin			//Se pasa al sigueinte estado con S_IN=0                             
                 if (~S_IN) begin 
                  nxt_state = 8'b00100000;
                  conv = 1'b0;
                 end
                 else nxt_state = 8'b00000010; //Se devuelve al estado 10
               end     

    8'b00100000: begin			//Se pasa al siguiente estado con S_IN=1                             
                 if (S_IN) begin
                  nxt_state = 8'b01000000;
                  conv = 1'b0;
                 end
                 else nxt_state = 8'b00000001; //Con S_IN=0 se va al IDLE
               end 

    8'b01000000: begin			//S_IN = 0 se pasa al siguiente estado                             
                 if (~S_IN) begin
                  nxt_state = 8'b10000000;
                  conv = 1'b0;
                 end
                 else nxt_state = 8'b00010000; //S_IN=1 se devuelve al estado 10000
               end                                                                           
               
    8'b10000000: begin			//Caracter de entrada recibo
                 conv = 1'b1;                      
                 if (~RESET) nxt_state = 8'b00000001; //Conve = 1
               end

    // Si la maquina entrara en un estado inesperado, regrese al inicio
    default:   nxt_state = 8'b00000001;
  endcase

end
endmodule

