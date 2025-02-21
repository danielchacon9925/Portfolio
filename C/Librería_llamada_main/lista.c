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
	@author Daniel Chacón-Delany Quirós
	@version 1
	@date 2021
	@param first_value primer dato de la lista.
	@param ptrpos_t Puntero que apunta a primer dato de la lista.
	@returns Puntero a primer dato.
	*/
	node *ptrpos_t=malloc(sizeof(node)); 
/**Se asigna espacio en memoria del tipo post_t*/
	if(ptrpos_t==NULL){
		return (0);
	}
	ptrpos_t->data= first_value;
	ptrpos_t->next=NULL;
	return ptrpos_t;
}
node* readList(const char* filePath){
	/**
	@brief Funcion que lee una lista.
	@authorDaniel Chacón-Delany Quirós
	@version 1
	@date 2021
	@param filePath es direccion de archivo binario.
	@returns No retorna nada.
	*/
	node *head=malloc(sizeof(node));
	if(head==NULL){
		return(0);
	}

	node *Pespacio=head;
	int b=0;
	int c=0;
	FILE *fp;
	fp=fopen(filePath,"r");
 /**Se abre archivo para solo lectura*/

	if(fp!=NULL){
		while(fscanf(fp,"%d\n",&c)>0){
			node *elemento=malloc(sizeof(node));
 /**Se asigna  memoria a siguiente elemento*/
			if(b==0){ /**Ingresar el primer elemento*/
				head->data=c;
				//Pespacio->next=NULL;
				free(elemento);
 /**Se debe de liberar memoria*/
			}
			if(elemento==NULL){
				return (0);
			}
			if(b==1){ /**Ingresar en el siguiente elemento*/
				elemento->data=c; /**Ingreso dato*/
				head->next=elemento;
				head=elemento;
				free(elemento); /**Libero memoria*/
			}
			if(b>1){
				elemento->data=c;
				head->next=elemento;
				head=elemento;
			}
			b++;
		}
	}else{
		printf("Error: no se pudo leer el archivo");
	}
	return Pespacio;
	fclose(fp);
}


void writeList(node* head, const char* filePath){
	/**
	@brief Funcion que escribe una lista en un archivo.
	@author Daniel Chacón-Delany Quiros
	@version 1
	@date 2021
	@param head es el puntero al primer elemento de la lista.
	@param filePath Recibe direccion de archivo destino.
	@returns No devuelve nada.
	*/
	FILE *fpe;
	fpe=fopen(filePath,"w");
 /**Se abre archivo y se da  permisos de escritura*/
	if(fpe!=NULL){
		fprintf(fpe,"%d\n",head->data); 
/**Se debe escribir primer elemento*/

	}else{
		printf("Error: no se pudo escribir primer elemento.");
	}
	while(head->next!=NULL){
 /**Se  recorren todos los datos*/
		head=head->next;
 /**Me muevo al siguiente elemento*/
		if(fpe!=NULL){
			fprintf(fpe,"%d\n",head->data); 
/**Se escribe siguiente dato*/
		}else{
			printf("Error: No se pudo escribir dato");
		}
	}
	fclose(fpe);
}


int push_back(node* head, int new_value){
	/**
	@brief Funcion que agrega un elemento al final de la lista
	@author Daniel Chacón-Delany Quiróś
	@version 1
	@date 2021
	@param head puntero que apunto al primer elemento de la lista.
	@param new_value Recibe nuevo valor a agregar.
	@returns Devuelve 0 si se agrego bien, 1 si no se pudo reservar memoria
	*/
	node *nuevopushb=malloc(sizeof(node)); 
/** Reservo memoria*/
	if(nuevopushb==NULL){
		return (1);
 /**Si no se pudo asignar memoria */
	}
	while(head->next != NULL){
/**Como el puntero apunta al primer elemento de la lista se recorre hasta final*/
/**Se recorre hasta encontrar null*/
		head=head->next; 
/**Siguiente valor*/
	}
	nuevopushb->data=new_value;
	nuevopushb->next=NULL;
	head->next=nuevopushb; 
/**Cambio direccion donde apunta*/
	return (0);
}


int push_front(node** head, int new_value){
	/**
	@brief Funcion que agrega un elemento al final de la lista
	@author Daniel Chacón-Delany Quiros
	@version 1
	@date 2021
	@param head puntero al primer elemento de la lista.
	@param new_value Recibe nuevo valor a agrergar.
	@returns Devuelve 0 si se agrego bien, 1 si no se pudo reservar memoria
	*/

	node *nuevopushFront=malloc(sizeof(node)); 
/**Se reserva  memoria */
	if(nuevopushFront==NULL){
		return(1);
	}
	nuevopushFront->data=new_value;
	nuevopushFront->next=*head;
/**Se apunta al primer elemento de la lista*/
	*head=nuevopushFront; 
/**Puntero senala el nuevo elemento de la lista*/
	return(0);
}


int pop_back(node* head){
	/**
	@brief Funcion que elimina el ultimo elemento de la lista
	@author Daniel Chacón-Delany Quiros
	@version 1
	@date 2021
	@param head Se recibe el puntero al primer elemento de la lista
	@returns Regresa el último valor almacenado en la lista.
	*/
	node *anterior;
	while(head->next!=NULL){
		anterior=head; 
/**Acceso al penultimo sitio en la lista*/
		head=head->next; 
/**Se recorre hasta el final de la lista*/
	}
	int valor;
	valor=head->data;
	free(head); /**Libero memoria */
	anterior->next=NULL; /**Asigno NULL al penultimo valor*/
	return valor;
}


int pop_front(node** head){
	/**
	@brief Funcion que elimina el primer elemento de la lista
	@author Daniel Chacón-Delany Quirós
	@version 1
	@date 2021
	@param **head recibe el puntero que apunta al primer elemento
	@returns Regresa el primer valor almacenado en la lista.
	*/
	int valor;
	node *liberar;
	liberar=(*head); 
/**Asigno puntero a primer elemento*/
	valor=(*head)->data; 
/**Guardo dato*/
	(*head)=(*head)->next; 
/**Puntero anterior a nuevo elemento*/
	free(liberar); 
/**Libero memoria*/
	return valor;
}


int insertElement(node** head, int pos, int new_value){
	/**
	@brief Funcion que ingresa un elemento en medio de la lista.
	@author Daniel Chacón-Delany Quiros
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
	@author Daniel Chacón-Delany Quiros
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
	@author Daniel Chacón-Delany Quiros
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
	@author Daniel Chacón-Delany Quiros
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
	@author Daniel Chacón-Delany Quiros
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
