#include "libreria.h"

int main(){

    printf("---------------------------\n");
    printf("-----TESTING FUNCTIONS-----\n");
    printf("---------------------------\n");

    ////////////////////
    // 1. Create list //
    ////////////////////
    printf("\n----1. LIST CREATION----\n");
    printf("First node created: \n");
    node *LIST_CREATED = CREATE_LIST(70);
    // Print list
    PRINT_LIST(LIST_CREATED);
    //___________________________________
    ///////////////////////////
    // 2. Read list from txt //
    ///////////////////////////
    printf("\n----2. READ LIST FROM TXT----\n");
    printf("Reading list from txt FILE: \n");
    node *LIST_GIVEN = READ_LIST("binarios.txt");
    // Print list
    PRINT_LIST(LIST_GIVEN);
    //___________________________________
    ///////////////////////////////////
    // 3. Write linked list to a txt //
    ///////////////////////////////////
    printf("\n----3. WRITE LIST TO TXT----\n");
    printf("Linked list to a txt: CHECK Linked_list_to_file.txt \n");
    WRITE_LIST(LIST_CREATED,"Linked_list_to_file.txt");
    //___________________________________
    /////////////////////////
    // 4. PUSH FRONT TEST //
    ////////////////////////
    printf("\n----4. PUSH FRONT TO LINKED LIST----\n");
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
    printf("\n----5. PUSH BACK TO LINKED LIST----\n");
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
    printf("\n----6. POP FRONT TO LINKED LIST----\n");
    int POP_FRONT_VALUE=POP_FRONT(&LIST_CREATED);
    printf("The value POP FRONT is %d\n",POP_FRONT_VALUE);
    printf("The remaining list is: \n");
    PRINT_LIST(LIST_CREATED);
    //___________________________________
    //////////////////////
    // 7. POP BACK TEST //
    //////////////////////
    printf("\n----7. POP BACK TO LINKED LIST----\n");
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
    printf("\n----8. INSERT ELEMENT TO LINKED LIST----\n");
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
    printf("\n----9. REMOVE ELEMENT FROM LINKED LIST----\n");
    int POSITION_TO_REMOVE = 19;
    printf("The position to free is %d\n",POSITION_TO_REMOVE);
    int VALUE_REMOVED=REMOVE_ELEMENT(&LIST_CREATED,POSITION_TO_REMOVE);
    printf("The value removed is %d\n",VALUE_REMOVED);
    printf("The remaining list is: \n");
    PRINT_LIST(LIST_CREATED);
    // COUNT ELEMENTS//
    int COUNT_1 = COUNT_NODES(LIST_CREATED);
    printf("The node count is %d\n", COUNT_1);
    //___________________________________
    ////////////////////////////////
    // 10. GET ELEMENT by POSITION//
    ////////////////////////////////
    printf("\n----10. GET ELEMENT USING POSITION FROM LINKED LIST----\n");
    // DEBUG FROM SEGMENTATION ERROR
    //printf("DEBUG: Printing full list before GET_ELEMENT\n");
    // print_debug(LIST_CREATED);
    int VALID;
    int POSITION_TO_GET = 10;
    printf("The position to GET is %d\n",POSITION_TO_GET);
    int GET_VALUE=GET_ELEMENT(LIST_CREATED,POSITION_TO_GET,VALID);
    //___________________________________
    /////////////////////
    // 11. SORT POSITION//
    /////////////////////
    printf("\nLIST BEFORE SORTING\n");
    PRINT_LIST(LIST_CREATED);
    printf("\nSORTING DESCENDING\n");
    SORT(LIST_CREATED,'D');
    PRINT_LIST(LIST_CREATED);
    printf("\nSORTING ASCENDING\n");
    SORT(LIST_CREATED,'A');
    PRINT_LIST(LIST_CREATED);
    //___________________________________
    ///////////////////
    // 12. CLEAN LIST//
    ///////////////////
    printf("\nLIST BEFORE CLEAN\n");
    PRINT_LIST(LIST_CREATED);
    int FREE_LIST = CLEAN_LIST(&LIST_CREATED);
    if (FREE_LIST == 1){
        printf("The list have NOT been cleaned by the function CLEAN_LIST\n");
    } else {
        printf("The list have  been cleaned by the function CLEAN_LIST\n");
    }
    int COUNT_2 = COUNT_NODES(LIST_CREATED);
    printf("The node count is %d\n", COUNT_2);
    PRINT_LIST(LIST_CREATED);
    return (0);
}