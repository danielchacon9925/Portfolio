module testerescritura(CLK, MDC, RESET, MDIO_START, MDIO_OUT, MDIO_OE, MDIO_IN, T_DATA, RD_DATA, DATA_RDY);

//Entradas
output reg CLK, RESET, MDIO_START, MDIO_IN;
output reg [31:0] T_DATA;

//Salida
input wire [15:0] RD_DATA;
input wire DATA_RDY, MDC, MDIO_OE, MDIO_OUT;

//Reloj
        always #2 CLK = ~CLK;
//Valores de testbench
integer i=0, seed;

initial begin
        $dumpfile("testMDIO.vcd");
        $dumpvars();
//Valores iniciales
        CLK <= 1;
        RESET <= 0;
        #5
        RESET <= 1;
        MDIO_START <= 1;
        T_DATA <= 32'h0x51115F1F; //Valor de prueba que indica lectura
        for (i=0;i<70;i=i+1)begin
                #3 seed = $urandom%2;
                MDIO_IN = seed;
        end
        #100;
        RESET <= 0;
        #20;

        $finish;
end

endmodule
