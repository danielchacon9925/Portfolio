// Implementation file: contains the actual code for the functions declared in the header files
#include "lista.h"
#include <stdio.h>

/**
 *		front
 * 	_________________
 * 	|_____head______|
 * 	|_______________|
 * 	|_______________|
 * 	|_______________|
 *  |_____tail______|
 *
 * 		back
 **/

node* createList(int first_value){
	/**
	@brief Funcion que crea lista.
	@author Daniel Chacón
	@version 1
	@date 2021
	@param first_value primer dato de la lista.
	@param ptrpos_t Puntero que apunta a primer dato de la lista.
	@returns Puntero a primer dato.
	*/
	// Pointer for the allocated memory enough to hold the node structure
	node *ptrpos_t=malloc(sizeof(node)); 
	// Error handling & end case
	if(ptrpos_t==NULL){
		return (0);
	}
	//Node initialization
	ptrpos_t->data= first_value;
	ptrpos_t->next=NULL;
	return ptrpos_t;
}
node* readList(const char* filePath){
	/**
	@brief Funcion que lee una lista.
	@author Daniel Chacón
	@version 1
	@date 2021
	@param filePath es direccion de archivo binario.
	@returns No retorna nada.
	*/
	node *head=malloc(sizeof(node));
	if(head==NULL){
		return(0);
	}

	// Pointer for the head
	node *Pespacio=head;

	// Counter index list
	int b=0;
	// Next value
	int c=0;

	// FILE: Structure in stdio- Contains info acout file such as position
	FILE *fp;

	// Open file for reading
	fp=fopen(filePath,"r");

	// Check if file is opened successfully
	if(fp!=NULL){
		// Read integers from file and stores in C
		while(fscanf(fp,"%d\n",&c)>0){
			// Memory allocation for a new node
			node *elemento=malloc(sizeof(node));
 			// Memory allocation for new element
			if(b==0){ // First integer being processed
				// C is assigned to data in the head node
				head->data=c;
				//Pespacio->next=NULL;
				free(elemento); // Should be removed?
 			/**Se debe de liberar memoria*/
			}
			if(elemento==NULL){
				return (0);
			}
			if(b==1){ // Handle the second element in the list
				elemento->data=c;  // Assign the integer value from the file to the new node
				head->next=elemento; // Link the previous node to the new node
				head=elemento; // Move head to point to the new node
				free(elemento); // Should be removed?
			}
			if(b>1){ // Handle the third or later integer in the list
				elemento->data=c; // Assign the integer value from the file to the new node
				head->next=elemento; // Link the previous node to the new node
				head=elemento; // Move head to point to the new node
			}
			b++;
		}
	}else{
		printf("Error: no se pudo leer el archivo");
	}
	return Pespacio;
	fclose(fp);
}


// New logic to try
/**
node* readList(const char* filePath) {
    // Allocate memory for the head node
    node* head = malloc(sizeof(node));
    if (head == NULL) {
        return NULL;  // Return NULL if memory allocation fails
    }

    // Pointer to track the head of the list
    node* Pespacio = head;

    // Counter to track the number of integers processed
    int b = 0;

    // Variable to store the integer read from the file
    int c = 0;

    // Open the file for reading
    FILE* fp = fopen(filePath, "r");
    if (fp == NULL) {
        printf("Error: no se pudo leer el archivo\n");
        free(head);  // Free the allocated memory before returning
        return NULL;
    }

    // Read integers from the file and construct the linked list
    while (fscanf(fp, "%d", &c) == 1) {
        if (b == 0) {  // First integer being processed
            head->data = c;  // Assign the integer to the head node
            head->next = NULL;  // Initialize next pointer to NULL
        } else {
            // Allocate memory for a new node
            node* elemento = malloc(sizeof(node));
            if (elemento == NULL) {
                printf("Error: no se pudo asignar memoria\n");
                fclose(fp);  // Close the file before returning
                return Pespacio;  // Return the list constructed so far
            }

            // Assign the integer to the new node
            elemento->data = c;
            elemento->next = NULL;

            // Link the new node to the list
            head->next = elemento;
            head = elemento;  // Move head to the new node
        }
        b++;  // Increment the counter
    }

    // Close the file
    fclose(fp);

    // Return the head of the linked list
    return Pespacio;
}
*/








void writeList(node* head, const char* filePath){
	/**
	@brief Funcion que escribe una lista en un archivo.
	@author Daniel Chacón
	@version 1
	@date 2021
	@param head es el puntero al primer elemento de la lista.
	@param filePath Recibe direccion de archivo destino.
	@returns No devuelve nada.
	*/
	FILE *fpe;
	// Open file for writing 
	fpe=fopen(filePath,"w");
	// Check if file is opened successfully
	if(fpe!=NULL){
		// First node data is written to file
		fprintf(fpe,"%d\n",head->data); 
	}else{
		printf("Error: no se pudo escribir primer elemento.");
	}
	while(head->next!=NULL){
 	// Traverse the link list
		head=head->next;
		if(fpe!=NULL){
			fprintf(fpe,"%d\n",head->data); 
		// New data written
		}else{
			printf("Error: No se pudo escribir dato");
		}
	}
	fclose(fpe);
}
// New logic to try
/**
void writeList(node* head, const char* filePath) {
    // Open the file for writing
    FILE* fpe = fopen(filePath, "w");
    if (fpe == NULL) {
        printf("Error: no se pudo abrir el archivo %s\n", filePath);
        return;
    }

    // Traverse the linked list and write each element to the file
    node* current = head;  // Use a temporary pointer to traverse the list
    while (current != NULL) {
        fprintf(fpe, "%d\n", current->data);  // Write the data to the file
        current = current->next;              // Move to the next node
    }

    // Close the file
    fclose(fpe);
}
*/

int push_back(node* head, int new_value){
	/**
	@brief Funcion que agrega un elemento al final de la lista
	@author Daniel Chacón
	@version 1
	@date 2021
	@param head puntero que apunto al primer elemento de la lista.
	@param new_value Recibe nuevo valor a agregar.
	@returns Devuelve 0 si se agrego bien, 1 si no se pudo reservar memoria
	*/
	// Pointer for new item
	node *nuevopushb=malloc(sizeof(node)); 
	// Check if memory allocation was successfull
	if(nuevopushb==NULL){
		return (1);
 	// Failed to allocate memory
	}
	while(head->next != NULL){
		// Check every element of the list until NULL found
		head=head->next; 
	}
	// Link new push to data for the new value
	nuevopushb->data=new_value;
	// Next element indicates end of listy
	nuevopushb->next=NULL;
	// Linked previus element to the new push
	head->next=nuevopushb; 
	return (0);
}

// New logic to try
/**
int push_back(node* head, int new_value) {
    // Allocate memory for the new node
    node* nuevopushb = malloc(sizeof(node));
    if (nuevopushb == NULL) {
        return 1;  // Return 1 if memory allocation fails
    }

    // Initialize the new node
    nuevopushb->data = new_value;
    nuevopushb->next = NULL;

    // Handle empty list case
    if (head == NULL) {
        head = nuevopushb;  // If the list is empty, the new node becomes the head
        return 0;
    }

    // Traverse to the end of the list
    node* current = head;  // Use a temporary pointer to traverse the list
    while (current->next != NULL) {
        current = current->next;
    }

    // Link the new node to the end of the list
    current->next = nuevopushb;

    return 0;  // Return 0 on success
}
 */

int push_front(node** head, int new_value){
	// Dpuble pointer to the head
	/**
	@brief Funcion que agrega un elemento al final de la lista
	@author Daniel Chacón
	@date 2021
	@param head puntero al primer elemento de la lista.
	@param new_value Recibe nuevo valor a agrergar.
	@returns Devuelve 0 si se agrego bien, 1 si no se pudo reservar memoria
	*/

	node *nuevopushFront=malloc(sizeof(node)); 
	// Check if memory was allocated successfully
	if(nuevopushFront==NULL){
		return(1);
	}
	// Linked push front to new data
	nuevopushFront->data=new_value;
	// Set to point to the current head of the list
	nuevopushFront->next=*head;
	// Updates the head pointer to the new element added on the front.
	*head=nuevopushFront; 
	return(0);
}

// New logic to try
/**
int push_front(node** head, int new_value) {
    // Allocate memory for the new node
    node* nuevopushFront = malloc(sizeof(node));
    if (nuevopushFront == NULL) {
        return 1;  // Return 1 if memory allocation fails
    }

    // Initialize the new node
    nuevopushFront->data = new_value;
    nuevopushFront->next = *head;  // Link the new node to the current head

    // Update the head pointer to point to the new node
    *head = nuevopushFront;

    return 0;  // Return 0 on success
}
 */

int pop_back(node* head){
	/**
	@brief Funcion que elimina el ultimo elemento de la lista
	@author Daniel Chacón
	@version 1
	@date 2021
	@param head Se recibe el puntero al primer elemento de la lista
	@returns Regresa el último valor almacenado en la lista.
	*/
	node *anterior;
	// Traverse all the elements of the list
	while(head->next!=NULL){
		// Anterior updated to point the current node
		anterior=head; 
		// Head is moved to the next node
		head=head->next; 
	}
	// Define data type for the pop back
	int valor;
	// Stores the value of the last node on value
	valor=head->data;
	// Deallocated memory for last element
	free(head); 
	// Point to the last value NULL
	anterior->next=NULL; 
	// Returned last value
	return valor;
}

// New logic to try
/**
int pop_back(node* head) {
    // Handle empty list
    if (head == NULL) {
        printf("Error: La lista está vacía.\n");
        return -1;  // Return an error value
    }

    // Handle single-node list
    if (head->next == NULL) {
        int valor = head->data;
        free(head);  // Free the only node
        head = NULL;  // Update head to NULL (note: this won't affect the caller)
        return valor;
    }

    // Traverse to the second-to-last node
    node* anterior = NULL;
    while (head->next != NULL) {
        anterior = head;
        head = head->next;
    }

    // Store the value of the last node
    int valor = head->data;

    // Free the last node
    free(head);

    // Update the second-to-last node to point to NULL
    anterior->next = NULL;

    return valor;
}
 */

int pop_front(node** head){
	/**
	@brief Funcion que elimina el primer elemento de la lista
	@author Daniel Chacón
	@version 1
	@date 2021
	@param **head recibe el puntero que apunta al primer elemento
	@returns Regresa el primer valor almacenado en la lista.
	*/
	// Data type where is stored
	int valor;
	// Pointer to free data
	node *liberar;
	// Pointer to the pointer head
	liberar=(*head); 
	//	Value from the head stored on valor
	// valor = liberar->data
	valor=(*head)->data; 
	// Update pointer to the next element
	// liberar = liberar -> next
	(*head)=(*head)->next; 
	// Popfirst
	free(liberar); 
	// Return popped value
	return valor;
}


int insertElement(node** head, int pos, int new_value){
	/**
	@brief Funcion que ingresa un elemento en medio de la lista.
	@author Daniel Chacón
	@version 1
	@date 2021
	@param **head puntero que apunta al primer elemento
	@param pos Recibe posicion donde se desea insertar elemento.
	@param new_value Recibe valor a ingresar.
	@returns Regresa 0 si se agrego correctamente o 1 si no se encontro direccion.
	*/
	node *lugar=(*head); 
/**Puntero que se va a modificar*/
	int i=0;
	node *nuevoelem=malloc(sizeof(node)); 
/**Se asigna  memoria*/
	if(nuevoelem==NULL){
		return (1); 
/**No se puede asignar memoria */
	}
	nuevoelem->data=new_value; /**Ingreso el dato*/

	for(i=0;i<pos;i++){
		if(pos==0){
			/**Se busca insertar al inicio*/
			return push_front(head, new_value);
 /**Llamo a push_front y paso parametros*/
		}
		if(pos-1<i){
/**Si no se encontro la ubicacion*/
			return 1;
		}
		if(pos-1==i){
/**El contador inicia en 0, se le  resta 1 como prueba*/
			nuevoelem->next=lugar->next; 
/**Nuevo elemento apunta al puntero anterior */
			lugar->next=nuevoelem; 
/**Puntero anterior apunta a nuevo elemento*/
			return (0);
		}
		if(pos-1>i){
/**No se ha encontrado la ubicacion deseada*/
			lugar=lugar->next; 
/**Proxima direccion a verificar*/
		}
	}
}


int removeElement(node** head, int pos){
	/**
	@brief Funcion que elimina un elemento en medio de la lista.
	@author Daniel Chacón
	@version 1
	@date 2021
	@param **head Puntero que apunta al puntero del primer elemento
	@param pos Recibe posicion donde se desea eliminar elemento.
	@returns Regresa valor borrado o -1 si dio error.
	*/
	int valor;
	node *liberar=(*head);
	node *anterior=(*head);
	int i=0;

	while(anterior->next!=NULL){
		/**Para recorrer toda la lista*/
		if(pos-1<i){
			return -1; 
/**Hubo un error, no se encontro ubicacion*/
		}
		if(pos-1==i){
			valor=liberar->data;/**Guardo dato*/
			anterior->next=liberar->next;
 /**Ingresar direccion a que apuntaba el eliminado*/
			free(liberar);
 /**Libero memoria*/
			return valor;
		}
		if(pos-1>i){
			/**No se ha encontrado la ubicacion deseada*/
			anterior=liberar; 
/**Apunto a struct, valor anterior*/
			liberar=liberar->next; 
/**Me muevo al siguiente elemento*/
			i++;
		}
	}






}



int freeList(node* head){
	/**
	@brief Funcion que libera memoria.
	@author Daniel Chacón
	@version 1
	@date 2021
	@param *head Recibe el puntero al primer elementode la lista
	@returns Regresa 0 para indicar correcta liberacion.
	*/
	while(head->next!=NULL){
		node *liberar;
		liberar=head; /**Para modificar puntero al primer elemento*/
		head=head->next; /**Me muevo a siguiente elemento*/
		free(liberar); /**Libero memoria*/
	}
	free(head); /**Libero memoria*/
	return (0);
}

int getElement(node* head, int index, int* valid){
	/**
	@brief Funcion que obtiene un elemento en medio de la lista.
	@author Daniel Chacón
	@version 1
	@date 2021
	@param *head Se recibe el puntero al primer elementode la lista
	@param index Recibe posicion donde se desea obtener elemento.
	@param *valid Puntero usado para identificar valor valido.
	@returns Regresa valor obtenido.
	*/

	node *elegido=head; 
/**Puntero por  mover*/
	int valorget=0;
	int i=0;
	while (elegido->next!=NULL){
		if(index-1==i){ 
/**Valor buscado*/
			valorget=elegido->data;
			(*valid)=0;
			return valorget;
		}
		if(index==0){ /**Se busca primer valor*/
			valorget=elegido->data;
			(*valid)=0;
		}
		if(index-1>i){ /**Se busca en siguiente elemento*/
			elegido=elegido->next;
			i++;
			(*valid)=0;
		}
		if(index-1<i){ /**No se encontró*/
			(*valid)=1;
			break;
		}
	}





}
int printElement(const int value){
	printf("%d \n", value);
	return 0;
}

void sort(node* head, char dir){
	/**
	@brief Funcion que reordena la lista.
	@author Daniel Chacón
	@version 1
	@date 2021
	@param *head  puntero al primer elemento de la lista
	@param dir caracter que indica orden
	@returns No retorna nada.
	*/
	node *sort=head;
	node *siguiente=head->next;
	int i=0;
	int respaldo=0;
	if(dir=='a'){ /**Ordenar acendente*/
		for(i=0;i<1000;i++){
			while(sort->next!=NULL){
				if((sort->data)>(siguiente->data)){
					respaldo=siguiente->data;
					siguiente->data=sort->data;
					sort->data=respaldo;
/**Se deben mover punteros para comparar los que siguen*/
					sort=sort->next;
					siguiente=siguiente->next;
				}	else if((sort->data)<(siguiente->data)){
/*Compara con el siguiente elemento,se deben mover punteros*/
					sort=sort->next;
					siguiente=siguiente->next;
				}
			}
/**Se colocan punteros al inicio de nuevo*/
			sort=head;
			siguiente=head->next;
		}
	}else if(dir=='d'){ /**Ordenar de manera descendente*/
		for(i=0;i<1000;i++){
			while(sort->next!=NULL){
				if((sort->data)<(siguiente->data)){ 
					respaldo=sort->data;
					sort->data=siguiente->data;
					siguiente->data=respaldo;
					/**Se deben mover punteros para siguiente comparacion*/
					sort=sort->next;
					siguiente=siguiente->next;
				}	else if((sort->data)>(siguiente->data)){
					/**Se deben mover punteros igual para siguiente comparacion*/
					sort=sort->next;
					siguiente=siguiente->next;
				}
			}
			/**Se colocan punteros al inicio de nuevo*/
			sort=head;
			siguiente=head->next;
		}
	}else if(dir!='a' || dir!='d'){ /**No es un caracter valido, no se debe hacer nada*/
		printf("No se digito un caracter valido, debe digitar a o d\n" );
	}
}


void printList(node* head){
	/**
	@brief Funcion que Imprime la lista.
	@author Daniel Chacón
	@version 1
	@date 2021
	@param *head puntero al primer elemento de la lista
	@param dato Puntero de respaldo a mover.
	@returns No retorna nada.
	*/
	node *dato=head;  /**Creo puntero de tipo pos*/
	while(dato!=NULL){
		/**Imprime mientras el ultimo elemento no apunte a nulo*/
		printf("%d\n",dato->data);
		dato=dato->next; /**Ingreso en dato (num y dir) la dire y el numero que estan en la posicion que apunta next*/
	}
	printf("\n");
}
