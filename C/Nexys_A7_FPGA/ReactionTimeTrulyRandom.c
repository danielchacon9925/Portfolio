#define GPIO_SWs 0x80001400
#define GPIO_LEDs 0x80001404
#define GPIO_INOUT 0x80001408

#define READ_GPIO(dir) (*(volatile unsigned *)dir)
#define WRITE_GPIO(dir, value)                 \
    {                                          \
        (*(volatile unsigned *)dir) = (value); \
    }

/* Inclusión de bibliotecas para printfNexys() */
#if defined(D_NEXYS_A7)
#include <bsp_printf.h>
#include <bsp_mem_map.h>
#include <bsp_version.h>
#else
PRE_COMPILED_MSG("no platform was defined")
#endif
#include <psp_api.h>

#include <stdio.h>

/*Inclusión de librería rand*/
#include <stdlib.h>

// Definición de delay y cantidad N de iteraciones de Fibonacci. Se utiliza N+1=12+1 para que llegue al valor de 144 de Fibonacci
#define DELAY 1500000

void IOsetup();
unsigned int getSwitchesVal();
void writeValtoLEDs(unsigned int val);
void delay(int num);
unsigned int decToBin(unsigned int decimal);
int a;

// Condiciones Iniciales: A nivel empírico se ha determinado que un segundo corresponde a 4 millones de ciclos de la función Delay

int main(void)
{
    unsigned int switches_val;
    unsigned int init_code;
    unsigned int end_code;
    int n = 1;
    unsigned int Xms = 0;

    int aleatorio;
    // Iniciar UART
    uartInit();
    IOsetup();
    while (1)
    {

        /* Se inicia con los LEDs encendidos */
        writeValtoLEDs(0xFFFFFFFF);

        /* Adquirimos valores de switches */
        switches_val = getSwitchesVal();

        /* Aplicamos máscara */
        init_code = (switches_val & 0x00000001);
        end_code = 0;


        // Iniciamos detectando si el usuario ha bajado el interruptor
        if (init_code == 0)
        {
            
            
            /*El programa apaga todos los LEDS */
            writeValtoLEDs(0x00000000);
            switches_val = getSwitchesVal();

            // Generamos valor realmente aleatorio
            srand(Xms);
            aleatorio = rand() % 3 + 1;

            /*Y espera un tiempo aleatorio menor a 3s*/
            delay(aleatorio);
            n = 0;


            /*Se inicia medición de tiempo*/
            writeValtoLEDs(0xFFFFFFFF);

            while(end_code == 0)
            {
                switches_val = getSwitchesVal();
                end_code = (switches_val & 0x00000001);
                n++; // Variable para contar el tiempo hasta que el usuario sube el interruptor
            }

            /*Aplicamos regla de 3 empírica para tiempo de reacción en ms*/
            Xms = (2000* n)/6000000; 

            writeValtoLEDs(Xms);

            delay(1);

            printfNexys("Tiempo transcurrido: %d ms\nValor aleatorio: %d \n", Xms, aleatorio);
            
            delay(6);
        }    
    }
}

void IOsetup()
{
    int En_Value = 0xFFFF;
    WRITE_GPIO(GPIO_INOUT, En_Value);
}

unsigned int getSwitchesVal()
{
    unsigned int val;

    val = READ_GPIO(GPIO_SWs); // read value on switche
    val = val >> 16;           // shift into lower 16 bits

    return val;
}

void writeValtoLEDs(unsigned int val)
{
    WRITE_GPIO(GPIO_LEDs, val); // display val on LEDs
}

void delay(int num)
{
    for (int j = 0; j < num * 6000000; j++)
    {
        a++;
    };
}