// Laboratorio 1-Daniel Chacón Mora-B72018
// El programa cumple la función de obtener números aleatorios al usar un push button para un bingo.
// Funciones para generación de delay, números random, imprimir y verificar que no hayan repetidos

#include <pic14/pic12f683.h>

/* WDT OFF*/
typedef unsigned int word;
word __at 0x2007 __CONFIG = (_WDTE_OFF & _WDT_OFF & _MCLRE_OFF);


void delay (unsigned time);
unsigned int random(unsigned int min, unsigned int max);
void print(int value, int display);
int isNumberInArray(unsigned int *array, unsigned int size, unsigned int number);


void main(void)
{
	TRISIO = 0b00010000; // GP4 como entrada por default
	GPIO = 0x00; //Todos los pines en bajo

	unsigned int time = 10;
	unsigned int num_1, num_2;
	unsigned int ganador;
	unsigned int bolas = 0;

    // Array que almacena valores obtenidos
    unsigned int ganadores[1];

	while( 1 )
	{
		// valores random para cada 7Seg
		num_1 = random(0,9);
		num_2 = random(0,9);

		// Se muestran valores random en display
		print(num_1, 0);
		delay(time);
		print(num_2, 1);
		delay(time);

		// Push button
		if(GP4)  
		{
			while (GP4)
			{
				print(num_1, 0);
				delay(time);
				print(num_2, 1);
				delay(time);

                // Concatenar num_1 y num_2 y guardar en el array
				ganador=num_1 * 10 + num_2;

                if (!isNumberInArray(ganadores, bolas+1, ganador))
                {
                    // Guardar el valor solo si no está en el array
                    ganadores[bolas+1] = ganador;

                    bolas = bolas + 1;
                }

                bolas = bolas + 1;

			}
		}

		// Cantidad máxima de bolas alcanzada
		if (bolas == 10)
		{
			// Primer 99 blink
			print(9, 0);
			delay(time);
			print(9, 1);
			delay(time);
			// Segundo 99 blink
			print(9, 0);
			delay(time);
			print(9, 1);
			delay(time);
			// Tercer 99 blink
			print(9, 0);
			delay(time);
			print(9, 1);
			delay(time);

			// Cantidad de bolas reiniciadas
			bolas = 0;

		}
	}
}

/* Función para números aleatorios*/
unsigned int random(unsigned int min, unsigned int max)
{
	// Se define valor inicial
    static unsigned int rand = 999; 

    rand += ((rand * rand) /100) % 10000;

	// Se calcula valores dentro de rango definido
    return rand % (max+1-min)+min;

}

/* Función que muestra números en displays*/

void print(int value, int display)
{
    if (display == 0)
	{
		if (value == 0) GPIO = 0b00000000;

		else if (value == 1) GPIO = 0b00000001; 

		else if (value == 2) GPIO = 0b00000010; 

		else if (value == 3) GPIO = 0b00000011;

		else if (value == 4) GPIO = 0b00000100;

		else if (value == 5) GPIO = 0b00000101;

		else if (value == 6) GPIO = 0b00000110;

		else if (value == 7) GPIO = 0b00000111;

		else if (value == 8) GPIO = 0b00010000;

		else GPIO = 0b00010001;
	}

	else  // display == 1
	{
		if (value == 0) GPIO = 0b00100000;

		else if (value == 1) GPIO = 0b00100001; 

		else if (value == 2) GPIO = 0b00100010; 

		else if (value == 3) GPIO = 0b00100011;

		else if (value == 4) GPIO = 0b00100100;

		else if (value == 5) GPIO = 0b00100101;

		else if (value == 6) GPIO = 0b00100110;

		else if (value == 7) GPIO = 0b00100111;

		else if (value == 8) GPIO = 0b00110000;

		else GPIO = 0b00110001;
	}
}

/* DElAY*/
void delay(unsigned int time)
{
	unsigned int i;
	unsigned int j;

	for(i=0;i<time;i++)
	  for(j=0;j<1275;j++);
}

/* Función que verifica si un número ya está en el array */
// Se utiliza el contador de "bolas" para indicar posición de array.
int isNumberInArray(unsigned int *array, unsigned int size, unsigned int number)
{
    for (unsigned int i = 0; i < size; ++i)
    {
        if (array[i] == number)
        {
            // El número ya está en el array
            return 1; // Verdadero
        }
    }

    // El número no está en el array
    return 0; // Falso
}