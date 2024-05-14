/*
Archivo Ejercicio_5
Estudiantes:
    Daniel Chacón Mora – B72018
    Alejandro Ulate Arce – B97926

Descripción:
    Este archivo realiza las siguientes acciones:
    - Se imprime I SAY HI utilizando los 8 digitos de los segmentos
*/

// Memory directions
#define RPTC_CNTR 0x80001200
#define RPTC_HRC 0x80001204
#define RPTC_LRC 0x80001208
#define RPTC_CTRL 0x8000120C
#define SegEn_ADDR 0x80001038
#define SegDig_ADDR 0x8000103C

/*
#define Seg_Digit0_ADDR    0x80001038
#define Seg_Digit1_ADDR    0x80001039
#define Seg_Digit2_ADDR    0x8000103A
#define Seg_Digit3_ADDR    0x8000103B
#define Seg_Digit4_ADDR    0x8000103C
#define Seg_Digit5_ADDR    0x8000103D
#define Seg_Digit6_ADDR    0x8000103E
#define Seg_Digit7_ADDR    0x8000103F
*/

#define READ(dir) (*(volatile unsigned *)dir)

#define WRITE(dir, value) { (*(volatile unsigned *)dir) = (value); }

int main(void)
{
    // Enable 8 displays
    WRITE(SegEn_ADDR, 0x00);
    // Counter start
    WRITE(RPTC_CNTR, (0x0));
    // MAX value for 1seg=0x2FFFFFFF
    WRITE(RPTC_LRC, 0x100);
    // Counter Enable
    WRITE(RPTC_CTRL, (0x21));

    int interrupt;
    // Visualize display
    int num = 0;

    while (1)
    {
        // Read Value from control register and extract bit INT
        interrupt = ((READ(RPTC_CTRL) >> 6) & 0b1);
        WRITE(SegDig_ADDR, num);

        // If bit high. RPTC_CNTR=RPTC_LRC
        if (interrupt == 1)
        {
            // Counter up
           num += 1;
           WRITE(SegDig_ADDR, num);
           
        }
        
        // Set bit value to 0
        WRITE(RPTC_CTRL, 0X21);
        
    }
    return 0;
}