#include "lista.h"
int main (){
   /**
   @brief Función principal aquí se llaman las funciones.
   @author Delany Quirós-Daniel Chacón
   @param listacreada Recibe puntero devuelto por createList.
   @param valorback Recibe 0 o 1 para verificar funcionamiento.
   @param valorfront Recibe 0 o 1 para verificar funcionamiento.
   @param valorpopb Recibe valor eliminado.
   @param valor Recibe valor eliminado.
   @param valorinsert Recibe 0 o 1 para verificar funcionamiento.
   @param valorremove Recibe valor eliminado. o -1 en caso de error.
   @param valorgetelement Recibe elemento deseado.
   @param valid Recibe 0 o 1 para verificar funcionamiento.
   @param ptrvalid Puntero a valid para enviar a funcion.
   @param posicion Posicion de elemento deseado.
   @returns Un 0 que indica buen funcionamiento.
   */
   printf("Creando la lista\n");


   /**Primer paso: Crear lista*/
   node *listacreada=createList(70);


   /**Prueba de impresión*/
   printList(listacreada);


   /**Prueba de push_back*/
   int valorback=0;
   printf("Esta es una prueba para push_back\n");
   valorback=push_back(listacreada,55);
   if(valorback==1){
      printf("Error al añadir\n");
   }
   valorback=push_back(listacreada,78);
   if(valorback==1){
      printf("Error al añadir\n");
   }
   valorback=push_back(listacreada,900);
   if(valorback==1){
      printf("Error al añadir\n");
   }
   printList(listacreada);


   /** Prueba de push_front*/
   int valorfront=0;
   printf("Esta es una prueba para push_front\n");
   push_front(&listacreada,1);
   if(valorfront==1){
      printf("Error al añadir\n");
   }
   push_front(&listacreada,2);
   if(valorfront==1){
      printf("Error al añadir\n");
   }
   push_front(&listacreada,3);
   if(valorfront==1){
      printf("Error al añadir\n");
   }
   printList(listacreada);


   /**Prueba pop_back*/
   int valorpopb=0;
   printf("Esta es una prueba para funcion pop_back\n");
   valorpopb=pop_back(listacreada);
   printList(listacreada);
   printf("El valor eliminado es: %d\n",valorpopb);

   /**Prueba pop_front*/
   int valor=0;
   printf("Esta es una prueba para funcion pop_front\n");
   valor=pop_front(&listacreada);
   printList(listacreada);
   printf("El valor eliminado es: %d\n",valor);


   /**Prueba funcion insertElement*/
   printf("Esta es una prueba para funcion insertElement\n");
   int valorinsert=0;
   valorinsert=insertElement(&listacreada,3,20);
   printList(listacreada);
   if(valorfront==1){
      printf("Error al añadir\n");
   }


   /** Prueba removeElement*/
   printf("Esta es una prueba para funcion removeElement\n");
   int valorremove=0;
   valorremove=removeElement(&listacreada,3);
   printList(listacreada);
   if(valorremove==-1){
      printf("Error al eliminar valor.\n");
   } else{
      printf("El valor eliminado es: %d\n",valorremove);
   }


   /**Prueba getElement*/

   int valorgetelement=0;
   int valid=0;
   int *ptrvalid=&valid;
   int posicion=4;

   printf("Esta es una prueba para funcion getElement\n");
   valorgetelement=getElement(listacreada,posicion,ptrvalid);
   printf("El valor %d de la lista es: %d\n",posicion,valorgetelement);
   if(valid==0){
      printf("Valor aceptado\n");
   }
   if(valid==1){
      printf("Valor no aceptado\n");
   }


   /**Prueba sort*/
   sort(listacreada,'d');
   printf("De manera descendente la lista es:\n");
   printList(listacreada);


   sort(listacreada,'a');
   printf("De manera ascendente la lista es:\n");
   printList(listacreada);


   /**Prueba readList*/
   printf("Se lee la lista dada.\n");
   node *listadada=readList("/IE0117/Laboratorios/Lab7/lab7/src/binario.txt");
   printList(listadada);


   /**Prueba writeList*/
   printf("La lista se escribe en un archivo plano\n");
   writeList(listacreada,"Salida.txt");


   /**Prueba freeList*/
   freeList(listacreada);
   freeList(listadada);
   printf("Se libero memoria ocupada por las listas.\n");


   return 0;

}
