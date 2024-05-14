/*
IE0424: Laboratorio de Circuitos Digitales I
Laboratorio 6 Ejercicio Básico 1

Estudiantes
Daniel Chacón Mora – B72018
Alejandro Ulate Arce – B97926
Erick Sancho Alvarado - B87388

El siguiente programa realiza lo siguiente:
- Utiliza el display de 7 segmentos para desplegar valores de ejes X, Y, Z
*/


// Direcciones Accelerometro
#define SPCR 0x80001100
#define SPSR 0x80001108
#define SPDR 0x80001110
#define SPER 0x80001118
#define SPCS 0x80001120

// Direcciones Display 7 Segmentos
#define SegEn_ADDR 0x80001038
#define SegDig_ADDR 0x8000103C

// Direcciones de ejes
#define X_ADDR 0x08
#define Y_ADDR 0x09
#define Z_ADDR 0x0A


#define READ(dir) (*(volatile unsigned *)dir)
#define WRITE(dir, value){(*(volatile unsigned *)dir) = (value);}


void spiInit(void)
{
    WRITE(SPCR, 0x0B);  // Se realiza una lectura del registro
    WRITE(SPER, 0x02);  // Especifica velocidad de reloj
}

void spiCS(unsigned int CS_status)
{
    if(CS_status) 
    {
        WRITE(SPCS, 0xFF); // o cargar 0x00
    }
    else
    {
        WRITE(SPCS, 0x00);
    }
}

unsigned int spiReadAxisData(unsigned int axis_address)
{
    //internalSpiClearIF()
    int val = READ(SPSR); // Se inicializa valor de interrupción

    // internalSpiActualSend()
    WRITE(SPDR, axis_address); // Pasamos dirección de registro del periférico

    //InternalSpiTestIF() 
    while (val != 0x80){    // Evaluamos interrupción hasta que finalice una transferencia
        val = READ(SPSR);
        val = val & 0x80; // Se extrae bit 7
    }

    //InternalSpiReadData()
    int axis_value = READ(SPDR);

    return axis_value;
}


int main(void)
{
    unsigned int eje_x, eje_y, eje_z;
    spiInit();
    spiCS(1);


    while(1)
    {
        eje_x = spiReadAxisData(X_ADDR);
        //eje_y = spiReadAxisData(Y_ADDR); 
        //eje_z = spiReadAxisData(Z_ADDR);

        WRITE(SegEn_ADDR, 0x00);
        WRITE(SegDig_ADDR, eje_x);
    }
    return 0;
}