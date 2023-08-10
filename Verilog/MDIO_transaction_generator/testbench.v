`include "testlectura.v"
`include "testescritura.v"
`include "DUT.v"

//Lectura

module lectura_tb;

//Entradas
wire CLK, RESET, MDIO_START, MDIO_IN;
wire [31:0] T_DATA;

//Salidas
wire [15:0] RD_DATA;
wire DATA_RDY, MDC, MDIO_OE, MDIO_OUT;

DUT MDIO(
.CLK            (CLK),
.MDC            (MDC),
.RESET          (RESET),
.MDIO_START     (MDIO_START),
.MDIO_OUT       (MDIO_OUT),
.MDIO_OE        (MDIO_OE),
.MDIO_IN        (MDIO_IN),
.T_DATA         (T_DATA),
.RD_DATA        (RD_DATA),
.DATA_RDY       (DATA_RDY)
);

testerlectura testlectura(
.CLK            (CLK),
.MDC            (MDC),
.RESET          (RESET),
.MDIO_START     (MDIO_START),
.MDIO_OUT       (MDIO_OUT),
.MDIO_OE        (MDIO_OE),
.MDIO_IN        (MDIO_IN),
.T_DATA         (T_DATA),
.RD_DATA        (RD_DATA),
.DATA_RDY       (DATA_RDY)
);

endmodule

//Escritura

module escritura_tb;

//Entradas
wire CLK, RESET, MDIO_START, MDIO_IN;
wire [31:0] T_DATA;

//Salidas
wire [15:0] RD_DATA;
wire DATA_RDY, MDC, MDIO_OE, MDIO_OUT;

DUT MDIO(
.CLK            (CLK),
.MDC            (MDC),
.RESET          (RESET),
.MDIO_START     (MDIO_START),
.MDIO_OUT       (MDIO_OUT),
.MDIO_OE        (MDIO_OE),
.MDIO_IN        (MDIO_IN),
.T_DATA         (T_DATA),
.RD_DATA        (RD_DATA),
.DATA_RDY       (DATA_RDY)
);

testerescritura testescritura(
.CLK            (CLK),
.MDC            (MDC),
.RESET          (RESET),
.MDIO_START     (MDIO_START),
.MDIO_OUT       (MDIO_OUT),
.MDIO_OE        (MDIO_OE),
.MDIO_IN        (MDIO_IN),
.T_DATA         (T_DATA),
.RD_DATA        (RD_DATA),
.DATA_RDY       (DATA_RDY)
);

endmodule

