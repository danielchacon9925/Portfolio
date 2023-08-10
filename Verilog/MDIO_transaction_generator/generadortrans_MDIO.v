module mdio(CLK,MDC, RESET, MDIO_START, MDIO_OUT, MDIO_OE, MDIO_IN, T_DATA, RD_DATA, DATA_RDY);

//Entradas
input wire CLK, RESET, MDIO_START, MDIO_IN;
input wire [31:0] T_DATA;

//Salidas
output reg [15:0] RD_DATA;
output reg DATA_RDY, MDC, MDIO_OE, MDIO_OUT;

//Variables internas
reg [5:0] count; //Contador para mitad de frecuencia
reg [5:0] nxt_count;
reg [15:0] nxt_RD_DATA; //Contador para saber valores contenidos en RD_DATA
reg nxt_DATA_RDY, nxt_MDC, nxt_MDIO_OE, nxt_MDIO_OUT;

//Clock divider

always @(posedge CLK)begin
        if(RESET == 0)begin
                MDC <= 0;
        end else begin
                MDC <= !MDC;
        end
end

//Definición de siguientes valores en cada MDC up 
always @(posedge MDC)begin
        count <= nxt_count;
        DATA_RDY <= nxt_DATA_RDY;
        MDIO_OE <= nxt_MDIO_OE;
        MDIO_OUT <= nxt_MDIO_OUT;
        RD_DATA[15:0] <= nxt_RD_DATA;
end

//Contador para transmisión de datos seriales
always @(posedge MDIO_START)begin
        count <= 31;
end


always @(*)begin
	//Valores iniciales
        nxt_count = count;
        nxt_DATA_RDY = 0;
        nxt_MDIO_OE = 0;
        nxt_MDIO_OUT = 0;
        nxt_RD_DATA[15:0] = RD_DATA[15:0];

        if(MDIO_START == 1 && count >= 0)begin
	
//Caso de escritura
        nxt_MDIO_OUT = T_DATA[count];  //Transacción de paralelo a serie
        if(count!=0)begin
                nxt_count = count - 1; //Contador ubica valores desde el bit más significativo
        end
        else begin
                nxt_count = count;     //Mantiene el valor que se pasa al flipflop
        end
        if(T_DATA[29:28]==2'b10 && count>15)begin //En lectura se mantiene señal en alto en primeros 16 bits
                nxt_MDIO_OE = 1;
        end
        else if (T_DATA[29:28]==2'b01)begin //En escritura se mantiene en alto en los 32 bits
                nxt_MDIO_OE = 1;
        end
        else begin
                nxt_MDIO_OE = 0;	//Luego de los 16 bits en lectura, se pone en cero
        end
//Caso de lectura
        if(T_DATA[29:28]==2'b10)begin
                if(count <= 15 && DATA_RDY!=1)begin //Cuando no se ha recibido recepción completa de palabra serial 
                        nxt_RD_DATA[15:0] = {RD_DATA[14:0],MDIO_IN};
                end

                if (count==0)begin
                        nxt_DATA_RDY = 1;
                end
        end
        if(count==0)begin
                nxt_MDIO_OE = 0; //Luego de los 32bits de lectura se pone en cero
        end
        end
end
endmodule







