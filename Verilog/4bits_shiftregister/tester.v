module Probador(S_OUT,clk,ENB,DIR,S_IN,MODO,D,Q);

// Salidas
input wire S_OUT;
input wire  [3:0] Q;

// Entradas
output reg clk, ENB, DIR, S_IN; 
output reg  [3:0] D;
output reg [1:0] MODO;

//Inicio testbench

    initial	clk <= 0;
    always begin
        #1 clk <= !clk;
    end

    initial begin
        // Se genera un display para cuando se corra el vvp 
        $dumpfile("testregistro.vcd");
        $dumpvars(0, testbench);
        $display("\t\t------------------------------------------");
        $display("\t\tTime\| clk \|  DIR  \|  S_IN \|  MODO  \| S_OUT");
        $display("\t\t------------------------------------------");
        $monitor( $time, "|\t%b |\t%b |\t%b |\t%b |\t%b ", clk, DIR, S_IN, MODO, S_OUT);
        
        // Rotación a la izquierda
            clk <= 1;
            ENB=0;
            #2
            ENB=1;
            D[3:0]=4'b0000;
            MODO[1:0]= 2'b10;
            DIR=0;
            S_IN=1;
            #2
            MODO[1:0]= 2'b00;
            #15
        // Reset    
            ENB=0;  
            S_IN=0;            
        // Rotación de a la derecha
            MODO[1:0]= 10;
            #2 
            ENB=1;
            D[3:0]=4'b00x0;            
            DIR=1;
            S_IN=1;
            #2
            MODO[1:0]=00;
            #15
 
        // Rotación circular a la izquierda
            MODO[1:0]= 10;
            #2 
            ENB=1;
            D[3:0]=4'b1010;            
            DIR=0;
            S_IN=1;
            #2
            MODO[1:0]=01;
            #15
        // Reset    
            ENB=0;  
            S_IN=0;   
        // Rotación circular a la derecha
            MODO[1:0]= 10;
            #2 
            ENB=1;
            D[3:0]=4'b0001;            
            DIR=0;
            S_IN=1;
            #2
            MODO[1:0]=01;
            #15  
        // Reset    
            ENB=0;  
            S_IN=0; 
        // Carga paralela
            MODO[1:0]= 10;
            #2 
            ENB=1;
            D[3:0]=4'b1001;            
            DIR=0;
            S_IN=1;
            #15
            $finish;
    end 


endmodule




