//Código de tarea para registro desplazable de 4 bits
//Daniel Chacón Mora-B72018

module registrodesplazable(S_OUT, clk, ENB, DIR, S_IN, MODO, D, Q);
	
// Input/Output definition
input wire clk;
input wire ENB;
input wire DIR;
input wire S_IN;
input wire [1:0] MODO;
input wire [3:0] D;
output reg [3:0] Q;
output reg S_OUT;

always @(posedge clk) begin

	if(ENB==1'b1) begin
		if (DIR==1'b0)begin	// Izquiera
			Q<=D;
			S_OUT<=0;
			case(MODO)
			2'b00: begin	// Rotación
				S_OUT <= Q[3];
				Q <= {Q[2:0],S_IN};
			end
			2'b01: begin	// Rotación circular
				Q <= {Q[2:0],Q[3]};
				S_OUT<=Q[3];
			end
			2'b10: begin	// Carga paralela
				Q <= D;
			end
			default: begin
				Q <= Q;
			end
			endcase
		end else if (DIR==1'b1)begin	// Derecha
			case(MODO)
			2'b00: begin	// Rotación
				Q <= {S_IN, Q[3:1]};
				S_OUT <= Q[0];
			end
			2'b01: begin	// Rotación circular
				Q <= {Q[0], Q[3:1]};
				S_OUT <= Q[0];
			end
			2'b10: begin	// Carga paralela
				Q <= D;
			end
			default: begin
				Q <= Q;
			end
			endcase		
		end

	end else begin
		Q <= D;
	end
	
end


endmodule
