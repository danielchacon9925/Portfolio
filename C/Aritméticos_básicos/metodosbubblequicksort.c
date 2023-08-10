/**     @file metodosbubblequicksort.c
 *      @brief El programa ordena descendientemente un arreglo de 1500 elementos
 *      @author Delany Quiros-Daniel Chacon
 *      
 *      @details Generar de forma aleatoria el arreglo de 0-100 y mostrar el tiempo 
 *      @bug Ninguno 
 *
 */


#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<unistd.h>

//Funcion para generar arreglo aleatorio

void arregloaleatorio(int *a, int n){
//Se define arreglo aleatorio de 0-100
	int i;
	for (i=0;i<n;i++)
	a[i]=rand()%100;
}
int mayor(int a[], int w){
	int i;
	
	int max=a[0];
	for(i=1;i<w;i++){
		if(a[i]>max){
			max=a[i];
		}
	}
	return max;
}
//Funcion para swap quicksort
void swap_elementos(int* primero, int* segundo) 
{ 
	int temp = *primero; 
	*primero = *segundo; 
	*segundo = temp; 
} 
//Funcion para particion con mayor y menor
int particion(int a[], int l, int w) 
{ 
	int p = a[w]; // pivot es el elemento mas grande
	int i = (l - 1); // Indice elemento mas pequeño 

	for (int j = l; j <= w- 1; j++) 
	{ 
		// If current element is smaller than the pivot 
		if (a[j] >  p) 
		{ 
			i++; 
			swap_elementos(&a[j], &a[i]); // swapping the elements
		} 
	} 
	swap_elementos(&a[i + 1], &a[w]); 
	return (i + 1);   
} 

void quick_sort(int a[], int l, int w) 
{ 
	if (l < w) 
	{ 
		int p_index = particion(a, l, w); 
		quick_sort(a, l, p_index - 1); 
		quick_sort(a, p_index + 1, w); 
	} 
} 
//Funcion para encontrar mayor
void main(){
        double tiempo_transcurrido=0.0;
	double tiempo_transcurrido1=0.0;
        clock_t begin = clock();
        sleep(3);
        clock_t end = clock();
        clock_t begin1 = clock();
        sleep(3);
        clock_t end1 = clock();

//Calcula tiempo por diferencia 
        tiempo_transcurrido += (double)(end-begin)/CLOCKS_PER_SEC;
	tiempo_transcurrido1 +=(double)(end1-begin1)/CLOCKS_PER_SEC; 
	int a[1500],n,i,j,temp;
	printf("Ingrese tamaño del arreglo:\n");
	scanf("%d",&n);
	arregloaleatorio(a,n);
//Mostrar arreglo aleatorio por medio de Bubblesort
	printf("\nEl arreglo aleatorio:");
	for(i=0;i<n;i++)
	printf(" %d ",a[i]);
	for(i=1;i<n;i++){
		for(j=0;j<n-1;j++){
			if(a[j+1]>a[j]){
			temp=a[j];
			a[j]=a[j+1];
			a[j+1]=temp;
			}
		}
	}

//Mostrar arreglo organizado de forma descendiente
	printf("\n\n");
	printf("\nEl arreglo organizado de forma descendiente usando Bubblesort:");
	for(i=0;i<n;i++)
	printf(" %d ",a[i]);
	printf("\n\n");
	printf("El tiempo de ejecucion es %f segundos\n",tiempo_transcurrido);
	int w= sizeof(a)/sizeof(a[0]);
	printf("Valor mas grande es %d, el cual sera usado como pivot para Quicksort\n",mayor(a,w));
	quick_sort(a, 0, n-1);
	printf("\nEl arreglo organizado de forma descendiente usando quicksort:"); 
        for(i=0;i<n;i++)
        printf(" %d ",a[i]);
        printf("\n\n");
	printf("El tiempo de ejecucion es %f segundos\n",tiempo_transcurrido1);

}
	
