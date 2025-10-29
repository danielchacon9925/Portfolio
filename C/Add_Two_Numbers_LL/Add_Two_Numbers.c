#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//===================
// Struct definition=
//===================
typedef struct node{
    int data;
    // Pointer to next value
    struct node *next;
}node;
//____________________________
//=============================
// Create a random X size list=
//=============================
node* RANDOM_LIST(int SIZE){
    // Error handling
    if (SIZE <= 0){
        printf("Cant create a list equal or less than 0");
        return NULL;
    }

    // Head pointer
    node *head=(node *)malloc(sizeof(node));
    // Pointer to traverse the list
    node *current = head; 
    // Error handling
    if (head == NULL){
        printf("Unable to allocate memory");
        return NULL;
    }
    //////////////////////////
    // Fields initialization//
    //////////////////////////
    // Data
    head->data = rand() % 10;
    // Next node
    head->next = NULL; 
    ///////////////////
    // Node creations//
    ///////////////////
    for (int i = 0; i < SIZE; i++){
        // Memory allocation for new node
        node *new_node = (node *)malloc(sizeof(node));
        // Error handling
        if (new_node == NULL){
            printf("Unable to allocate new node");
            return head;
        }
        ///////////////////////////////////////
        // Fields initialization for new node//
        ///////////////////////////////////////
        new_node->data = rand() % 10;
        new_node->next = NULL;
        ///////////////////////
        // Linked to the list//
        ///////////////////////
        // Link the new node
        current->next = new_node;
        // Update current pointer to new node added
        current = new_node;
    }
    // Return pointer to head of list
    return head;
}
//____________________________
//=============
// Count nodes=
//=============
int COUNT_NODES(node *head){
    // Counter 
    int count = 0;
    // Pointer to hold head pointer 
    node *current = head; 
    ///////////////////////
    // Traverse link list//
    ///////////////////////
    while(current != NULL){
        // Increment count
        count++;
        // Update current pointer
        current=current->next;
    }  
    // Return count
    return count; 
}
//____________________________
//=====================
// Evalaute alloc size=
//=====================
int ALLOC_SIZE(int L1_COUNT, int L2_COUNT){

    int MAX_NODES = (L1_COUNT>L2_COUNT) ? L1_COUNT : L2_COUNT;

    int SIZE = MAX_NODES + 1;

    printf("The size to alloc is: %d\n", SIZE);
    
    return SIZE;
}
//==============
// Add two nums=
//==============
node* addTwoNumbers(node* L1, node* L2) {
    //=============
    // Count nodes=
    //=============
    // Node count L1
    int L1_COUNT = COUNT_NODES(L1);
    // Node count L2
    int L2_COUNT = COUNT_NODES(L2);
    // Alloc size
    int SIZE_TO_ALLOC = ALLOC_SIZE(L1_COUNT, L2_COUNT);
    //==============
    // DEBUG PRINTS=
    //==============
    printf("Node count L1 %d\n",L1_COUNT);
    printf("Node count L2 %d\n",L2_COUNT);
    printf("SIZE_TO_ALLOC %d\n",SIZE_TO_ALLOC);
    //======================
    // FIELD INITIALIZATION=
    //======================
    // SUM RESULT
    node *SUM_RESULT = (node *)malloc(sizeof(node));
    // Error handling
    if (SUM_RESULT == NULL){
        printf("Unable to allocate memory");
        return NULL;
    }
    SUM_RESULT->data = 0;
    SUM_RESULT->next = NULL;
    // Pointer to traverse the list
    node *current = SUM_RESULT;
    // Carry
    int carry = 0;
    ///////////////////
    // Node creations//
    ///////////////////
    for(int i = 0; i<SIZE_TO_ALLOC-1; i++){

        if(current != NULL || carry != 0){

        // Check if space if empty, if so, add a 0
        int VALUE_1 = (L1 != NULL) ? L1->data : 0;
        int VALUE_2 = (L2 != NULL) ? L2->data : 0;

        printf("Data en L1 %d\n", VALUE_1);      
        printf("Data en L2 %d\n", VALUE_2); 
        
        // Data calculation
        int SUMA_index =  VALUE_1 + VALUE_2 + carry;
        // Carry calculation
        carry = SUMA_index/10;
        // Digit
        int digit = SUMA_index % 10;

        printf("EL resultado es: %d\n", digit);

        //////////////////////////
        // Fields initialization//
        //////////////////////////       
        node *NEW_NODE= (node *)malloc(sizeof(node));
        // Error handling
        if (NEW_NODE == NULL){
            printf("Unable to allocate memory");
            return NULL;
        }
        // Data initialization
        NEW_NODE->data = digit;
        NEW_NODE->next = NULL;

        ///////////////////
        // NODE INSERTION//
        ///////////////////        
        // Perform insertion at the end of the list
        current->next = NEW_NODE;
        // Update pointer
        current=current->next;
        ///////////////////////////
        // Update pointers for LL//
        ///////////////////////////
            if (L1 != NULL){
                L1=L1->next;
            }
            if (L2 != NULL){
                L2=L2->next;
            }
        }
        //printf("Salió de loop en if\n");

    }
    // To avoid return the head (has a 0)
    return SUM_RESULT->next;
}
//____________________________
//============
// PRINT LIST=
//============
void PRINT_LIST(node* head){
    // Pointer to store original head address
    node *VALUE_TO_PRINT = head;

    // Print every element until find NULL
    while (VALUE_TO_PRINT != NULL){
        // Point to data space
        printf("%d\n", VALUE_TO_PRINT->data);
        // Update pointer to next node
        VALUE_TO_PRINT = VALUE_TO_PRINT->next; 
    }
    printf("\n"); 
}
//____________________________
//===========
// FREE_LIST=
//===========
void FREE_LIST(node *head){
    // Pointer to traverse the list
    node *current = head;
    // Temporary variable to save next node
    node *next_node;
    while(current != NULL){
        // Pointer pointing to next node
        next_node = current->next;
        // Free current node
        free(current);
        // Update current to next node
        current = next_node; 
    }
}


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
    node *LIST_CREATED_L1 = RANDOM_LIST(5);
    PRINT_LIST(LIST_CREATED_L1); 
    printf("\n----2. LIST CREATION----\n");
    printf("Second node created: \n");
    node *LIST_CREATED_L2 = RANDOM_LIST(3);
    PRINT_LIST(LIST_CREATED_L2);
    printf("===============================\n");

    node *PROTO_FUN = addTwoNumbers(LIST_CREATED_L1,LIST_CREATED_L2);

    PRINT_LIST(PROTO_FUN);  
    FREE_LIST(LIST_CREATED_L1);
    FREE_LIST(LIST_CREATED_L2);
    FREE_LIST(PROTO_FUN);


}