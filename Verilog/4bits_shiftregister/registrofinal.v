//Código de tarea para registro desplazable de 4 bits
//Daniel Chacón Mora-B72018

module registrodesplazable(S_OUT,clk,ENB,DIR,S_IN,MODO,D,Q);

        input clk;
        input ENB;
        input DIR;
        input S_IN;
        input [1:0] MODO;
        input [3:0] D;
        output reg [3:0] Q;
        output reg S_OUT;

always @ (posedge clk)
begin
	if (ENB==1)begin
		//Rotación hacia la izquierda
		if (DIR==0 && MODO==2'b00)
			begin
			Q <= {Q[2:0],S_IN};
			S_OUT <= Q[0];
			end
		//Rotación hacia la derecha 
		else if (DIR==1 && MODO==2'b00)begin
			Q <= {S_IN,Q[3:1]};
			S_OUT <= Q[3];
			end
		//Rotación circular a la izquierda
		else if (DIR==0 && MODO==2'b01)
			Q[3:0] <= {Q[2:0],Q[3]};
		//Rotación circular a la derecha
		else if (DIR==1 && MODO==2'b01)
			Q[3:0] <= {Q[0],Q[3:1]};
		//Carga en paralelo
		else if ( MODO==2'b10)
			Q[3:0] <= D[3:0];
		else 
		Q[3:0]<=Q[3:0];
		end
	else 
		Q[3:0]<=Q[3:0];
end
endmodule
