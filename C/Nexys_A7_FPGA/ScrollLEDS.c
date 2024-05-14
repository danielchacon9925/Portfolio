/*
Ejercicio 3 Laboratorio 1

Archivo ScrollLEDS.c
Estudiantes:
    Daniel Chacón Mora – B72018
    Alejandro Ulate Arce – B97926

Descripción:
    Este archivo realiza las siguientes acciones:
    - Define los registros de entrada y salida del GPIO
    - Itera a lo largo de los registros del LED en subida y bajada
    encendiendolos incrementalmente hasta que se enciendan todos
    los registros y luego se detiene.
*/

/* Definiciones generales para lectura de GPIO para delay*/
#define GPIO_SWs 0x80001400
#define GPIO_LEDs 0x80001404
#define GPIO_INOUT 0x80001408
#define READ_GPIO(dir) (*(volatile unsigned *)dir)
#define WRITE_GPIO(dir, value)                 \
    {                                          \
        (*(volatile unsigned *)dir) = (value); \
    }

/* Función Principal */
int main(void)
{
    // Definir primeros 16 bits del registro como salida
    int En_Value = 0xFFFF, switches_value;

    WRITE_GPIO(GPIO_INOUT, En_Value);

    int i;
    int j = 0;
    int subida = 0x0001;
    int bajada = 0x8000;
    int n = 1;

    // Nuevo valor
    int ciclo = 0;

    // Valor inicial en subida
    int inicio = 0x0001;
    // Valor final en bajada
    int final = 0x8000;

    // Ciclo para que se repita las 16 veces
    for (ciclo = 0; ciclo < 16; ciclo++)
    {
        subida = inicio;
        bajada = final;

        while (j < 16) // subida
        {
            // Segundo recorrido de 16 LEDs
            WRITE_GPIO(GPIO_LEDs, subida);
            subida = subida << 1;

            j++;
            // Delay
            for (i = 0; i < 500000; i++)
            {
                switches_value = READ_GPIO(GPIO_SWs);
            };
        };

        while (j < 32) // bajada
        {
            // Primer recorrido de 16 LEDs
            WRITE_GPIO(GPIO_LEDs, bajada);
            bajada = bajada >> 1;
            j++;

            // Delay
            for (i = 0; i < 500000; i++)
            {
                switches_value = READ_GPIO(GPIO_SWs);
            };
        };

        // Condiciones para incrementar
        inicio = (1 << (n + 1)) - 1;
        final = (0x8000 >> n) + final;

        n++;
        j = 0;
    };

    return (0);
}