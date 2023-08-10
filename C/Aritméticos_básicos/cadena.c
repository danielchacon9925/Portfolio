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
    char line[150];
    int vocales, consonantes, digitos, espacios;

    vocales = consonantes = digitos = espacios = 0;

    printf("Ingrese linea de texto que desea analizar: ");
    fgets(line, sizeof(line), stdin);

    for (int i = 0; line[i] != '\0'; ++i) {
        if (line[i] == 'a' || line[i] == 'e' || line[i] == 'i' ||
            line[i] == 'o' || line[i] == 'u' || line[i] == 'A' ||
            line[i] == 'E' || line[i] == 'I' || line[i] == 'O' ||
            line[i] == 'U') {
            ++vocales;
        } else if ((line[i] >= 'a' && line[i] <= 'z') || (line[i] >= 'A' && line[i] <= 'Z')) {
            ++consonantes;
        } else if (line[i] >= '0' && line[i] <= '9') {
            ++digitos;
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
