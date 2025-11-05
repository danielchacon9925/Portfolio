#include "Deep_Copy.h"

////////////////////////
// 1. List generation //
////////////////////////
// Create a random list
node* RANDOM_LIST(int SIZE){
    // Error handling
    if (SIZE <= 0){
        printf("Cant create a list equal or less than 0\n");
        return NULL;
    }
    // Head pointer
    node **node_array=(node **)malloc(SIZE*sizeof(node*));
    // Pointer to traverse the list
    node *head = NULL;
    node *current = NULL; 
    ///////////////////
    // Node creations//
    ///////////////////
    for (int i = 0; i < SIZE; i++){
        // Memory allocation for new node
        node *new_node = (node *)malloc(sizeof(node));
        // Error handling
        if (new_node == NULL){
            printf("Unable to allocate new node");
            for (int k = 0; k < SIZE; k++){free(node_array[k]);}
            free(node_array);
            return NULL;
        }
        ///////////////////////////////////////
        // Fields initialization for new node//
        ///////////////////////////////////////
        new_node->val = rand() %100;
        new_node->next = NULL;
        new_node->random = 0;
        // Store pointers in array
        node_array[i]=new_node;
        // Link to the list
        // First link
        if (head == NULL) {
            head = new_node;
            current = new_node;
        } else { /*After first link*/
            current->next = new_node;
            current = new_node;
        }        
    }
    // Link the random pointer
    for (int i = 0; i < SIZE; i++) {
        // Random index in the range [0, SIZE - 1]
        int rand_index = rand()%(SIZE);
        printf("The random index chosen is: %d\n",rand_index);
        
        // Point the current node (node_array[i]) to the node at the random index
        node_array[i]->random = node_array[rand_index]->val;
    }
    // Return pointer to head of list
    free(node_array);
    return head;
}
//____________________________
//////////////////
// 2. List copy //
//////////////////
node* DEEP_COPY_LIST(node* head){
    //===========
    // LIST SIZE=
    //===========
    // Pointer to traverse the list
    node *current_ENTRYLIST = head;
    // Node count
    int SIZE = 0;
    while (current_ENTRYLIST != NULL)
    {
        SIZE++;
        // Value 
        //printf("Value in val space %d \n", current_ENTRYLIST->val);
        // Random
        //printf("Value pointed by random pointer %d \n", current_ENTRYLIST->random);       
        // Update pointer
        current_ENTRYLIST = current_ENTRYLIST->next;

    }
    free(current_ENTRYLIST);
    printf("Node count is: %d\n", SIZE);
    //======================
    // Pointer to the array=
    //======================
    node **node_array_COPY=(node **)malloc(SIZE*sizeof(node*));
    //printf("Doble pointer created \n");
    // Pointer to traverse the list
    //node *current = NULL; 
    //printf("current pointer pointing to null created \n");
    // Head pointer
    node *head_to_return = NULL;
    //printf("head_to_return pointer pointing to null created \n");
    // Pointer to traverse list while copy
    node *current_COPY = head;
    // Node creation
    for (int i = 0; i<SIZE; i++){
        // Create a new node
        node *new_node = (node *)malloc(sizeof(node));
        //printf("new node created, #: %d\n", i);
        // Error handling
        if (new_node==NULL){
            printf("Unable to allocate new node");
            for (int k = 0; k < SIZE; k++){free(node_array_COPY[k]);}
            free(node_array_COPY);
        }
        ///////////////////////////////////////
        // Fields initialization for new node//
        ///////////////////////////////////////
        //printf("FIELD INITIATION\n");
        new_node->val = current_COPY->val;
        new_node->next = current_COPY->next;
        new_node->random = current_COPY->random;
        node_array_COPY[i]=new_node;
        //Link to the list
        current_COPY->next = new_node;
        current_COPY = new_node;
    }
    free(node_array_COPY);
    return current_COPY;
}


//============
// PRINT LIST=
//============
void PRINT_LIST(node* head){
    // Pointer to store original head address
    node *VALUE_TO_PRINT = head;
    printf("{");
    // Print every element until find NULL
    while (VALUE_TO_PRINT != NULL){
        printf("[");
        // Point to data space
        printf("%d", VALUE_TO_PRINT->val);
        printf(",%d", VALUE_TO_PRINT->random);
        printf("]");
        // Update pointer to next node
        VALUE_TO_PRINT = VALUE_TO_PRINT->next; 
    }

    printf("}\n"); 
}

void PRINT_LIST_MATRIX(node *head) {
    if (head == NULL) {
        printf("List is empty.\n");
        return;
    }

    printf("\n--- Linked List Matrix (Val | Next Val | Random Val) ---\n");
    printf("-------------------------------------------------------\n");
    
    node *current = head;
    while (current != NULL) {
        // Column 1: Current node's value (val)
        printf("%8d", current->val);
        
        // Column 2: Next node's value (or -1 if NULL)
        printf("%11d", current->next ? current->next->val : -1);
        
        // Column 3: Random integer value (random_val)
        printf("%14d", current->random);
        
        printf("\n");
        current = current->next;
    }
    printf("-------------------------------------------------------\n");
}
