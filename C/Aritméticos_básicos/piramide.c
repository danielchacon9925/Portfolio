/**     @file piramide.c
 *      @brief Contiene un programa donde se crea una pirámide de números
 *	@author Delany Quirós-Daniel Chacón
 *
 *      @details El programa interactúa con el usuario, utiliza for para recorrer las filas y columnas de la pirámide.
 *      @bug aún no se sabe
 *
 */

/// Piramide de numeros

#include <stdio.h>

int main()
{
    int num, filas = 0, columnas = 0, indice = 0;

    printf( "Proporcione la altura de la pirámide: ");
    scanf("%d", &num);

    for(int i = 1; i <= num; ++i)
    {
        for(int libre = 1; libre <= num-i; ++libre)
        {
            printf("  ");
            ++filas;
        }

        while(indice != 2*i-1)
        {
            if (filas <= num-1)
            {
                printf("%d", i+indice); printf(" ");
                ++filas;
            }
            else
            {
                ++columnas;
                printf( "%d" , i+indice-2*columnas); printf (" ");
            }
            ++indice;
        }
        columnas =filas = indice = 0;

        printf("\n");
    }
    return 0;
}
