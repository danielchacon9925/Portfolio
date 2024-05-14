/*
Archivo Ejercicio_Basico_1.c
Estudiantes:    
    Daniel Chacón Mora – B72018
    Alejandro Ulate Arce – B97926

Descripción:
    Este archivo realiza las siguientes acciones:
    - Define los registros de entrada y salida del GPIO y SegEn_Addr
    para la habilitación de los registro digitales
    - Habilita los 4 dígitos de la derecha de la placa Nexys4DDR
    - Despliega el valor de los switches en los 4 dígitos de la derecha
    en hexadecimal.
*/

// memory-mapped I/O addresses
#define GPIO_SWs    0x80001400

// memory-mapped 7-Segment Display addresses
#define SegEn_ADDR    0x80001038
#define SegDig_ADDR   0x8000103C

#define WRITE_7Seg(dir, value) { (*(volatile unsigned *)dir) = (value); }
#define READ_GPIO(dir) (*(volatile unsigned *)dir)

#define DELAY 10000000
int switches_value, i, j;

int main ( void )
{

    // Enable values for 7 segment display
    WRITE_7Seg(SegEn_ADDR, 0xF0);

    // Initialize UART
    uartInit();

    while (1){      
        switches_value = READ_GPIO(GPIO_SWs);   // read value on switches   
        switches_value = switches_value >> 16;  // move value 16bits to the left
        WRITE_7Seg(SegDig_ADDR, switches_value); // print value on 7 segment display
    }
    return(0);
}

