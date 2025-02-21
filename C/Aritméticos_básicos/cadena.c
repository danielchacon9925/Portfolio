/**     @file cadena.c
 *      @brief Contiene un programa donde se cuentan las vocales, consonantes y digitos.
 *	@author Delany Quirós-Daniel Chacón
 *
 *      @details El usuario crea una frase de un máximo de 20 carácteres.
 *      @bug aún no se sabe
 *
 */


#include <stdio.h>

int main() {

    // Character array up to 150
    char line[150];
    int vocales, consonantes, digitos, espacios;

    // Counters
    vocales = consonantes = digitos = espacios = 0;

    // User interaction
    printf("Ingrese linea de texto que desea analizar: ");

    // Capture user text and store it on array, ensures size 150, specifies input comes from sdt input 
    fgets(line, sizeof(line), stdin);

    // Loop to iterate each character in the array until null character
    for (int i = 0; line[i] != '\0'; ++i) {
        // Check vocals
        if (line[i] == 'a' || line[i] == 'e' || line[i] == 'i' ||
            line[i] == 'o' || line[i] == 'u' || line[i] == 'A' ||
            line[i] == 'E' || line[i] == 'I' || line[i] == 'O' ||
            line[i] == 'U') {
            ++vocales;
        // Check if is a letter, if true is a consonant
        } else if ((line[i] >= 'a' && line[i] <= 'z') || (line[i] >= 'A' && line[i] <= 'Z')) {
            ++consonantes;
        // Check if is a number between 0 and 9
        } else if (line[i] >= '0' && line[i] <= '9') {
            ++digitos;
        // Check spaces
        } else if (line[i] == ' ') {
            ++espacios;
        }
    }

    printf("Vocales: %d\n", vocales);
    printf("Consonantes: %d\n", consonantes);
    printf("Digitos: %d\n", digitos);
    printf("Espacios en blaco: %d\n", espacios);
    return 0;
}
