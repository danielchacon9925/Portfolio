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
    printf("----5. PUSH BACK TO LINKED LIST----\n");
    int cont_2 = 71;
    int valor_PUSH_BACK;
    while(cont_2 < 81){
        valor_PUSH_BACK = PUSH_BACK(LIST_CREATED, cont_2);
        cont_2++;
    }
    PRINT_LIST(LIST_CREATED); 
    //___________________________________
    ///////////////////////
    // 6. POP FRONT TEST //
    ///////////////////////
    printf("----6. POP FRONT TO LINKED LIST----\n");
    int POP_FRONT_VALUE=POP_FRONT(&LIST_CREATED);
    printf("The value POP FRONT is %d\n",POP_FRONT_VALUE);
    printf("The remaining list is: \n");
    PRINT_LIST(LIST_CREATED);
    //___________________________________
    //////////////////////
    // 7. POP BACK TEST //
    //////////////////////
    printf("----7. POP BACK TO LINKED LIST----\n");
    int POP_BACK_VALUE=POP_BACK(&LIST_CREATED);
    printf("The value POP BACK is %d\n",POP_BACK_VALUE);
    printf("The remaining list is: \n");
    PRINT_LIST(LIST_CREATED);
    //___________________________________
    // COUNT ELEMENTS//
    int COUNT = COUNT_NODES(LIST_CREATED);
    printf("The node count is %d\n", COUNT);
    ///////////////////////
    // 8. INSERT ELEMENT //
    ///////////////////////
    int POSITION_TO_INSERT = 19;
    int VALUE_TO_INSERT = 80;
    printf("The value to insert is %d in the position %d\n",VALUE_TO_INSERT,POSITION_TO_INSERT);
    int NEW_VALUE_INSERTED=INSERT_ELEMENT(&LIST_CREATED,POSITION_TO_INSERT,VALUE_TO_INSERT);
    printf("The remaining list is: \n");
    PRINT_LIST(LIST_CREATED);
    // COUNT ELEMENTS//
    int COUNT_0 = COUNT_NODES(LIST_CREATED);
    printf("The node count is %d\n", COUNT_0);
    //___________________________________
    ///////////////////////
    // 9. REMOVE ELEMENT //
    ///////////////////////
    int POSITION_TO_REMOVE = 19;
    printf("The position to free is %d\n",POSITION_TO_REMOVE);
    int VALUE_REMOVED=REMOVE_ELEMENT(&LIST_CREATED,POSITION_TO_REMOVE);
    printf("The value removed is %d\n",VALUE_REMOVED);
    printf("The remaining list is: \n");
    PRINT_LIST(LIST_CREATED);
    // COUNT ELEMENTS//
    int COUNT_1 = COUNT_NODES(LIST_CREATED);
    printf("The node count is %d\n", COUNT_1);
    return (0);
}