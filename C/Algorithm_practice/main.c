#include "libreria.h"

int main(){

    printf("---------------------------\n");
    printf("-----TESTING FUNCTIONS-----\n");
    printf("---------------------------\n");

    ////////////////////
    // 1. Create list //
    ////////////////////
    printf("----1. LIST CREATION----\n");
    printf("First node created: \n");
    node *LIST_CREATED = CREATE_LIST(70);
    // Print list
    PRINT_LIST(LIST_CREATED);
    //___________________________________
    ///////////////////////////
    // 2. Read list from txt //
    ///////////////////////////
    printf("----2. READ LIST FROM TXT----\n");
    printf("Reading list from txt FILE: \n");
    node *LIST_GIVEN = READ_LIST("binarios.txt");
    // Print list
    PRINT_LIST(LIST_GIVEN);
    //___________________________________
    ///////////////////////////////////
    // 3. Write linked list to a txt //
    ///////////////////////////////////
    printf("----3. WRITE LIST TO TXT----\n");
    printf("Linked list to a txt: CHECK Linked_list_to_file.txt \n");
    WRITE_LIST(LIST_CREATED,"Linked_list_to_file.txt");
    //___________________________________
    /////////////////////////
    // 4. PUSH FRONT TEST //
    ////////////////////////
    printf("----4. PUSH FRONT TO LINKED LIST----\n");
    int cont_1 = 69;
    int valor_PUSH_FRONT;
    while(cont_1 > 59){
        // Expects double pointer. Is necessary to use address-of(&) operator
        valor_PUSH_FRONT = PUSH_FRONT(&LIST_CREATED, cont_1);
        cont_1--;
    }
    PRINT_LIST(LIST_CREATED); 
    //___________________________________
    ///////////////////////
    // 5. PUSH BACK TEST //
    ///////////////////////
    printf("----4. PUSH BACK TO LINKED LIST----\n");
    int cont_2 = 71;
    int valor_PUSH_BACK;
    while(cont_2 < 81){
        valor_PUSH_BACK = PUSH_BACK(LIST_CREATED, cont_2);
        cont_2++;
    }
    PRINT_LIST(LIST_CREATED); 
    return (0);
}