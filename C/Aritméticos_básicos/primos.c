/**     @file primos.c
 *      @brief Contiene un programa para determinar si un número es primo o no.
 *	@author Delany Quirós-Daniel Chacón
 *
 *	@details  Se utiliza for y las condicionales if y else.
 *      @bug aún no se sabe
 *
 */


#include<stdio.h>

int main()
{ 
	int num;
	printf("Por favor, ingrese un numero\n");
	scanf("%d",&num);
	
	int count=0;

	for(int i=2; i<num;i++)
	{
		if(num%i==0)
		count++;
	}
	
	if(count!=0)
	{
		printf("El numero digitado anterior no es primo\n");
	}
	else
	{
		printf("El numero digitado anterior es primo \n");
	}

	return 0;
}
