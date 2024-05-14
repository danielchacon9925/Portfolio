/* 
Ejercicio 2 Laboratorio 4

Archivo FlashSwitchesToLEDS_Functions.c
Estudiantes:    
    Daniel Chacón Mora – B72018
    Alejandro Ulate Arce – B97926

Descripción:
    Este archivo realiza las siguientes acciones
    - Lee el registro de entrada de los switches
    - Escribe el registro en la salida de los LEDS
    - Introduce delay de 2s para que los registros se alternen entre encendido y apagado
*/



#define GPIO_SWs 0x80001400
#define GPIO_LEDs 0x80001404
#define GPIO_INOUT 0x80001408

#define READ_GPIO(dir) (*(volatile unsigned *)dir)
#define WRITE_GPIO(dir, value)                 \
    {                                          \
        (*(volatile unsigned *)dir) = (value); \
    }

// Inclusión de bibliotecas importantes
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


void IOsetup();
unsigned int getSwitchesVal();
void writeValtoLEDs(unsigned int val);
void delay(int num, unsigned int switches_value);

int main(void)
{
    int n = 2;
    unsigned int switches_val;
    unsigned int reset = 0x0000;

    IOsetup();
    while (1)
    {
        switches_val = getSwitchesVal();


        delay(n, switches_val);
        writeValtoLEDs(switches_val);

        delay(n, switches_val);
        writeValtoLEDs(reset);
    }

    return (0);
}

void IOsetup()
{
    int En_Value = 0xFFFF;
    WRITE_GPIO(GPIO_INOUT, En_Value);
}

unsigned int getSwitchesVal()
{
    unsigned int val;

    val = (READ_GPIO(GPIO_SWs)); // read value on switche
    val = val >> 16;                          // shift into lower 16 bits

    return val;
}

void writeValtoLEDs(unsigned int val)
{
    WRITE_GPIO(GPIO_LEDs, val); // display val on LEDs
}

void delay(int num, unsigned int switches_value)
{
    	for (int j=0; j < num * 2000000; j++) {
            switches_value = READ_GPIO(GPIO_SWs);
        }   ;  
}