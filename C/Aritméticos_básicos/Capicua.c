/**	@file capicua.c
 *	@brief El programa analiza el numero ingresado para saber si es capicua o no 
 *	@author Delany Quiros-Daniel Chacon
 *	
 *	@details Buscar numero capicua
 *	@bug Ninguno 
 *
 */

#include<stdio.h>
int main(void){
//Definicion de variables
	int reverso,recuerdo,num,original,cociente,divisor,contador;
	cociente = 0;
	divisor = 1;
	contador = 0;
	printf("Ingrese el numero: \n");
	scanf("%d",&num);
	reverso=0;
	original=num;
	//Definicion de variables 
	while (cociente != 1){
		contador++;
		divisor = divisor*10;
		cociente = num/divisor;
		
		if(cociente == 1){
			printf("El numero tiene %d digitos\n",contador+1);
		}//fin de if
		if(cociente <1){
			printf("El numero tiene %d digitos\n", contador);
			cociente = 1;
		}//fin de if
		if(num < 10){
			printf("Solo tiene un digito\n");
		}//fin de if
	}
	//integro reverso es guardado en variable reverso
	while(num!=0){
	recuerdo = num%10;
	reverso = reverso*10 + recuerdo;
	num /= 10;
	}

	//Capicua si el original y el reverso son iguales
	if (original==reverso)
		printf("%d es un numero capicua\n",original);
	else
		printf("%d no es un numero capicua\n",original);
	return 0;
}
	
