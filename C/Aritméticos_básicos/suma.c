/**     @file suma.c
 *      @brief Contiene un programa donde se suman 1000 valores aleatorios pares
 *	@author Delany Quirós-Daniel Chacón
 *
 *      @details El programa interactúa con el usuario para conocer los límites de los números a sumar     
 *      @bug aún no se sabe
 *
 */


#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define max 1000
// Declaracion de funcion principal.
int main(void){
   srand(time(0));
  int i;
   int limi;
   printf("Por favor, ingrese limite inferior\n");
   scanf("%d",&limi);
   int lims;
   printf("Por favor, ingrese limite superior\n");
   scanf("%d",&lims);

   int sum = 0, num[max];
   FILE *fptr;
   // Declarando loop de 1000 numeros random
   for(i = limi; i <=lims; i++){
      //Guardar numeros en un arreglo.
      num[i] = rand() % 100 + 1;
      //Calcular suma de numeros aleatorios.
      sum+= num[i];
   }
   //Documento donde se guarda la sumatoria.
   fptr = fopen("numbers.txt", "w");
   //Comprobacion de documento puntero vacio o no 
   if(fptr == NULL){
      printf("Error!");
      exit(1);
   }
   fprintf(fptr, "La suma total en el arreglo es %d\n", sum); 
   fclose(fptr); // cerrar documento puntero
   printf("La suma de todos los valores aleatorios es %d\n",sum);
}
