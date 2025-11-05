#include "Deep_Copy.h"

int main(){
    // Seed for random numbers
    srand(time(NULL));

    printf("---------------------------\n");
    printf("-----TESTING FUNCTIONS-----\n");
    printf("---------------------------\n");

    ////////////////////
    // 1. Create list //
    ////////////////////
    printf("\n----1. LIST CREATION----\n");
    printf("First node created: \n");
    node *LIST_CREATED = RANDOM_LIST(4);
    // Print list
    PRINT_LIST(LIST_CREATED);    
    printf("Value pointed by random pointer: %d\n", LIST_CREATED->random);
    //PRINT_LIST_MATRIX(LIST_CREATED);

    printf("\n----2. LIST COPY----\n");
    node *DP_LIST = DEEP_COPY_LIST(LIST_CREATED);
    // Print list
    PRINT_LIST(DP_LIST);   
}