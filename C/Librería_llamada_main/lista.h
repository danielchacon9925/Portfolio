/** @file lista.h
 *  @brief Realiza la función de biblioteca, posee las funciones necesarias para que el programa main.c funcione correctamente.
 *
 *  @details ....
 */

#ifndef LISTA_HPP
#define LISTA_HPP

#include <stdio.h>
#include <stdlib.h>

typedef struct node {
	int data; //**< data */
	struct node* next; //**< pointer to next element */
} node;

/**
 *  @brief Representa cada elemento individual de la lista y con ellosse construye la lista completa. 
 *  @details Almacena un dato entero (int) y el puntero al siguiente elemento.
 *  @param ...
 *  @return ...
 **/
node* createList(int first_value);

/**
 *  @brief  regresa un puntero a una variable del tipo node y recibe el entero quese va a almacenar en la primera posici ́on de la lista.
 *  @details Debe reservar memoria solo para un elemento.
 *  @param ...
 *  @return ...
 **/
node* readList(const char* filePath);

/**
 *  @brief  Esta funcion regresa el puntero al primer elemento de la lista creada a partir del archivobinario ubicado en la ruta especificado por el parametro filePath.
 *  @details el archivo antes mencionado contieneuna lista de n ́umeros enteros separados por cambios de l ́ınea.
 *  @param ...
 *  @return ...
 **/
void writeList(node* head, const char* filePath);

/**
 *  @brief Esta funcion escribe una lista en un archivo de texto plano. 
 *  @details Cada elemento de la lista se escribira separado por un cambio de l ́ınea en el archivo de salida.
 *  @param ...
 *  @return ...
 **/
int push_back(node* head, int new_value);

/**
 *  @brief esta funcion regresa un entero que es 0 en caso de que el elemento se haya podidoa ̃nadir correctamente al final de la lista, o bien, 1 si no se pudo reservar memoria para el nuevo elemento de la lista. 
 *  @details recibe como par ́ametro el puntero al primer elemento de la lista, y el nuevo valor que se desea agregar.
 *  @param ...
 *  @return 0 or 1
 **/
int push_front(node** head, int new_value);

/**
 *  @brief esta funcion regresa un entero que es 0 en caso de que el elemento se haya podidoa ̃nadir correctamente al inicio de la lista, o bien, 1 si no se pudo reservar memoria para el nuevo elemento de la lista. 
 *  @details Recibe como par ́ametro el puntero al puntero que a punta al primer elemento de la lista, y elnuevo valor que se desea agregar.
 *  @param ...
 *  @return 0 or 1
 **/
int pop_back(node* head);

/**
 *  @brief esta funcion elimina la ultima posici ́on de la lista y adem ́as regresa el valor enteroque estaba almacenado en dicha posicion.
 *  @details  debe de hacer los cambios necesarios en la lista paraque siga siendo una lista enlazada valida.
 *  @param ...
 *  @return ...
 **/
int pop_front(node** head);

/**
 *  @brief esta funcion elimina la primera posici ́on de la lista y adem ́as regresa el valor enteroque estaba almacenado en dicha posicion.
 *  @details Recibe como par ́ametro el puntero al puntero que a punta al primerelemento de la lista. Debe liberar memoria.
 *  @param ...
 *  @return ...
 **/
int insertElement(node** head, int pos, int new_value);

/**
 *  @brief esta funcion agrega un elemento a la lista.
 *  @details Regresa 0 en caso de haber agregado correctamente el elemento, o 1 encaso de no poder localizar la memoria necesaria. 
 *  @param ...
 *  @return 0 or 1
 **/
int removeElement(node** head, int pos);

/**
 *  @brief esta funcion elimina un elemento de la lista. 
 *  @details Regresa el valor del elemento eliminado o -1 en caso de haber un error. Debe liberar memoria.
 *  @param ...
 *  @return -1
 **/
int freeList(node* head);

/**
 *  @brief esta funcion se encarga de liberar toda la memoria que haya sido localizada para la lista.
 *  @details Recibe como  ́unico par ́ametro el puntero al primer elemento de la lista.
 *  @param ...
 *  @return ...
 **/
int getElement(node* head, int index, int* valid);

/**
 *  @brief esta funcion se encarga de regresar el valor de un elemento espec ́ıfico de la lista.
 *  @details Un valor no sera valido en caso de que el usuario solicite una posici ́on que no existe en la lista.
 *  @param ...
 *  @return 0 or 1
 **/
int printElement(const int value);

/**
 *  @brief esta funcion se encarga de imprimir en consola un n ́umero entero seguido de unespacio, con cambios de lınea. 
 *  @details  Recibe como par ́ametro el n ́umero entero que desea imprimir.
 *  @param ...
 *  @return ...
 **/
void sort(node* head, char dir);

/**
 *  @brief ...
 *  @details ...
 *  @param ...
 *  @return ...
 **/
void printList(node* head);
/**
 *  @brief se encarga de imprimir toda la lista seguida de cambios de lınea.
 *  @details Recibe como parametro  ́unicamente el puntero al primer elemento de la lista.
 *  @param ...
 *  @return ...
 **/
#endif
