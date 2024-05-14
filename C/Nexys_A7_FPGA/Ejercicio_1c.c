/*
Archivo Ejercicio_Basico_1.c
Estudiantes:
    Daniel Chacón Mora – B72018
    Alejandro Ulate Arce – B97926

Descripción:
    Este archivo realiza las siguientes acciones:
    - Incrementa valor cada S y muestra en display de 8 bits
*/

// memory-mapped I/O addresses
#define GPIO_SWs 0x80001400

// memory-mapped 7-Segment Display addresses
#define SegEn_ADDR 0x80001038
#define SegDig_ADDR 0x8000103C

#define WRITE_7Seg(dir, value)                 \
    {                                          \
        (*(volatile unsigned *)dir) = (value); \
    }
#define READ_GPIO(dir) (*(volatile unsigned *)dir)

#define DELAY 10000000
// Inclusión de librerías
#include <stdio.h>
#include <time.h>

int switches_value, i, j, a, contador;
int n = 0;

// Declaración de función
void delay(int num);

void delay(int num)
{
    for (int j = 0; j < num * 6000000; j++)
    {
        a++;
    };
}

int main(void)
{

    // Enable values for 7 segment display
    WRITE_7Seg(SegEn_ADDR, 0x00);

    // Initialize UART
    uartInit();

    while (1)
    {
        contador = n;
        // switches_value = READ_GPIO(GPIO_SWs);    // read value on switches
        // switches_value = switches_value >> 16;   // move value 16bits to the left
        WRITE_7Seg(SegDig_ADDR, contador); // print value on 7 segment display
        delay(1);
        n++;
    }
    return (0);
}
