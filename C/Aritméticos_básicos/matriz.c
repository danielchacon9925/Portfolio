/**	@file matriz.c
 *	@brief Contiene un programa para decir si una matriz 3x3 es regular
 *	@author Delany Quirós-Daniel Chacón
 *
 *	@details El programa  interactúa con el usuario, utiliza variables enteras y flotantes, además obtiene el determinante de una matriz para decir su esta es regular o no con ayuda de los condicionales if y else.
 *	@bug aún no se sabe
 *
 */

#include <stdio.h>
#include <termios.h>
#include <stdlib.h>
#include <math.h>

///Para solicitar y crear la matriz a trabajar
int main()
{
    int matriz [3][3]={{0}},i,j;
    float determinante = 0;   
    for (i=0;i<3;i++)
    {
        for (j=0;j<3;j++)
        {
            printf("Introduzca el valor del lugar [%d][%d] de la matriz:\n ",i+1,j+1);
	    scanf("%d", &matriz[i][j]);
        }
    }

	printf("\n\t");
	printf("Esta es su matriz: ");
	
	for(i=0;i<3;i++)
		{
			printf("\n");
			for(j=0;j<3;j++)
	{
		printf("\t");
		printf("%d",matriz[i][j]);
		
		}

	}
		printf("\n");


///Para sacar el determinante

    
    for(i = 0; i < 3; i++)
    determinante = determinante + (matriz[0][i] * (matriz[1][(i+1)%3] * matriz[2][(i+2)%3] 
    - matriz[1][(i+2)%3] * matriz[2][(i+1)%3]));
    
	if(determinante!=0)
	{
    printf("La matriz es regular, posee inversa y su determinante es: %f\n", determinante);
 	}    
	else 
     {
     	 printf("La matriz no es regular\n");
	}
	return 0; 
}
