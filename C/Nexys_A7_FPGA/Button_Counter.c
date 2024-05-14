/*
Archivo Ejercicio_5
Estudiantes:
    Daniel Chacón Mora – B72018
    Alejandro Ulate Arce – B97926

Descripción:
    Este archivo realiza las siguientes acciones:
    - Utiliza los botones creados en el SwerVolfCore
    - Crea una cuenta ascendente que incrementa velocidad al presionar BTNC
    - Y resetea la cuenta utilizando el BTNU
*/

// memory-mapped I/O addresses

// Direcciones para direccionamiento de GPIO
#define GPIO2_INOUT 0X80001808
#define GPIO_INOUT 0X80001408

// Botones para ejercicio 3
#define GPIO2_BTNs 0x80001800

// Botones para ejercicio 4
#define SYSCON_BTNs 0x80001010

// Direccion de LEDS
#define GPIO_LEDs 0x80001404

// Para lectura y escritura en directorios
#define READ_GPIO(dir) (*(volatile unsigned *)dir)
#define WRITE_GPIO(dir, value) {(*(volatile unsigned *)dir) = (value);}      

// Delay
#define DELAY 0x1000000

void delay(int num);

int main(void)
{   
    int En_Value = 0xFFFF, En_Value_2 = 0x0000;
    int BTNU, BTNC;
    unsigned int counter = 0, delay_time = 6, button_pressed = 0;

    WRITE_GPIO(GPIO_INOUT, En_Value);
    WRITE_GPIO(GPIO2_INOUT, En_Value_2);

    while(1)
    {
        BTNC = (READ_GPIO(GPIO2_BTNs) & 0b1);
        BTNU = (READ_GPIO(SYSCON_BTNs) & 0b10);

        // Se aumenta la velocidad de la cuenta
        if (BTNC == 1 && button_pressed == 0)
        {
            button_pressed = 1;
            delay_time = delay_time - 1;
        }

        // Se resetea la cuenta ascendente
        if (BTNU == 2 && button_pressed == 0)
        {
            button_pressed = 1;
            counter = 0;
        }

        // Si el retardo llega a 0 en la cuenta rapida, se devuelve a la cuenta lenta
        if (delay_time == 0) 
        {
            delay_time = 6;
        }

        // Si no se apretan botones, la logica sigue esperando que se oprima boton
        if (BTNU == 0 && BTNC == 0) 
        {
            button_pressed = 0;
        }

        WRITE_GPIO(GPIO_LEDs, counter);
        delay(delay_time);
        counter++;
        
    }
    return 0;
}

void delay(int num)
{
    int a=800000;
    for (int j = 0; j < a*num; j++)
    {
        WRITE_GPIO(GPIO_INOUT, 0xFFFF);
    };
}