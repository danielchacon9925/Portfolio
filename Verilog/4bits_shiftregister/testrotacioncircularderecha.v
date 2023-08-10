/**Registro desplazable testbench*/

module registro_tb;


reg clk;
reg ENB;
reg DIR;
reg S_IN;
reg [1:0] MODO;
reg [3:0] D;

wire [3:0] Q;
wire S_OUT;

/** Instancia de registro DUT */

registrodesplazable dut(.S_OUT(S_OUT),.clk(clk),.ENB(ENB),.DIR(DIR),.S_IN(S_IN),.MODO(MODO),.D(D),.Q(Q));


initial begin
        $dumpfile("testregistro.vcd");
        $dumpvars(-1, dut);
        $monitor("D=%b,Q=%b,S_OUT=%b",D,Q,S_OUT);
end

//Inicio testbench

initial begin
//Testbench rotación a la izquierda
        clk=1;
        ENB=1;
        MODO[1:0]=10;
        DIR=1;
        S_IN=1;
        D[3:0]=4'b0001;
        #1;
        clk=0;
        #1;
        clk=1;
        MODO[1:0]=01;
        #1;
        clk=0;
        #1;
        clk=1;
/** Q[3:0]=0001 y S_OUT=0 */
        #1;
        clk=0;
	#1;
        clk=1;
        #1;
        clk=0;
        #1;
        clk=1;
        #1;
        clk=0;
        #1;
        clk=1;
        #1;
        clk=0;
        #1;
        clk=1;
        #1;
        clk=0;
        #1;
        clk=1;
        $finish;
end 
endmodule

