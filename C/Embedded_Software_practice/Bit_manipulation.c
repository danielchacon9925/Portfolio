// You are working with an 8-bit register
// 1. Set bit 3, 2. Clear bit 1, 3. Toggle bit 7, 4. return modified

#include <stdio.h>
#include <stdint.h> // Necessary for uint8_t
#include <stdlib.h>

uint8_t modify_register(uint8_t reg){

    // 1. Set bit 3
    reg = reg | (1 << 3);

    // 2. Clear bit 1
    // NAND mask 
    reg = reg & ~(1 << 1);

    // 3. Toggle bit 7
    // XOR mask
    reg = reg ^(1 << 7);

    return reg;
}

int main(){
    uint8_t initial_reg = 0b01000000;
    uint8_t final_reg = modify_register(initial_reg);

    printf("El registro inicial es: 0x%x\n",initial_reg);
    printf("El registro final es: 0x%x\n",final_reg);
}