`include "generadortrans_MDIO.v"

module DUT(CLK, MDC, RESET, MDIO_START, MDIO_OUT, MDIO_OE, MDIO_IN, T_DATA, RD_DATA, DATA_RDY);

//Entradas

input wire CLK, RESET, MDIO_START, MDIO_IN;
input wire [31:0] T_DATA;

//Salidas
output wire [15:0] RD_DATA;
output wire DATA_RDY, MDC, MDIO_OE, MDIO_OUT;

mdio inst1(

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
