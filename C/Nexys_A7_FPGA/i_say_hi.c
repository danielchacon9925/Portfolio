/*
Archivo Ejercicio_5
Estudiantes:
    Daniel Chacón Mora – B72018
    Alejandro Ulate Arce – B97926

Descripción:
    Este archivo realiza las siguientes acciones:
    - Se imprime I SAY HI utilizando los 8 digitos de los segmentos
*/

// Seven Segment Display Controller Registers
#define Seg_Digit0_ADDR    0x80001038
#define Seg_Digit1_ADDR    0x80001039
#define Seg_Digit2_ADDR    0x8000103A
#define Seg_Digit3_ADDR    0x8000103B
#define Seg_Digit4_ADDR    0x8000103C
#define Seg_Digit5_ADDR    0x8000103D
#define Seg_Digit6_ADDR    0x8000103E
#define Seg_Digit7_ADDR    0x8000103F

#define WRITE_7Seg(dir, value) { (*(volatile char *)dir) = (value); }

int main(void)
{   

    while(1)
    {

        WRITE_7Seg(Seg_Digit0_ADDR, 0b1111001);  // I

        WRITE_7Seg(Seg_Digit1_ADDR, 0b1001000);  // -

        WRITE_7Seg(Seg_Digit2_ADDR, 0b1111111);  // S

        WRITE_7Seg(Seg_Digit3_ADDR, 0b1000100);  // A

        WRITE_7Seg(Seg_Digit4_ADDR, 0b0001000);  // Y

        WRITE_7Seg(Seg_Digit5_ADDR, 0b0100100);  // -

        WRITE_7Seg(Seg_Digit6_ADDR, 0b1111111);  // H

        WRITE_7Seg(Seg_Digit7_ADDR, 0b1001111);  // I
        
    }
    return 0;
}