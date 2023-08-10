module Probador (P_VALID, P_OUT, S_OUT, CLK, RESET, S_IN, P_IN, S_START);

// Se definen las entradas del modulo
input P_VALID, S_OUT;
input [31:0] P_OUT;

// Se definen las salidas del modulo
output reg CLK, RESET, S_IN, S_START; 
output reg [31:0] P_IN ;

initial begin
        // Se ponen las entradas en sus estados iniciales

        #1
        RESET = 1;
        S_START = 0; 

        #2
        RESET = 1;
        S_START = 1;
        P_IN = 32'b00000000000000001111111111111111;

        #1 
	S_IN <= 1;
        #1 
	S_IN <= 0;
        #1 
	S_IN <= 1;
        #1 
	S_IN <= 1;
        #1 
	S_IN <= 0;
        #1 
	S_IN <= 1;
        #1 
	S_IN <= 0;

       
        #1 
	S_IN <= 1;
        #1 
	S_IN <= 1;
        #1 
	S_IN <= 1;
        #1 
	S_IN <= 1;
        #1 
	S_IN <= 1;
        #1 
	S_IN <= 1;
        #1 
	S_IN <= 1;
        #1 
	S_IN <= 1;
        #1 
	S_IN <= 1;
        #1 
	S_IN <= 1;
        #1 
	S_IN <= 1;
        #1 
	S_IN <= 1;
        #1 
	S_IN = 1;
        #1 
	S_IN = 1;
        #1 
	S_IN = 1;
        #1 
	S_IN = 1;
        #1 
	S_IN = 1;
        #1 
	S_IN = 1;
        #1 
	S_IN = 1;
        #1 
	S_IN = 1;
        #1 
	S_IN = 1;
        #1 
	S_IN = 1;
        #1 
	S_IN = 1;
        #1 
	S_IN = 1;
        #1 
	S_IN = 1;
        #1 
	S_IN = 1;
        #1 
	S_IN = 1;
        #1 
	S_IN = 1;
        #1 
	S_IN = 1;
        #1 
	S_IN = 1;
        #1 
	S_IN = 1;
        #1 
	S_IN = 1;

        #35 
	RESET = 0;
     

        #10
        $finish;
        end

    initial	CLK <= 0;
    always 
        begin
        #1 CLK <= !CLK;
        end      
endmodule
