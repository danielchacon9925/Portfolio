////////////////////////
// IMPLEMENTATION FILE//
////////////////////////

#include "libreria.h"
#include <stdio.h>

////////////////////////
// 1. List generation //
////////////////////////
// Create a list 
node* CREATE_LIST(int FIRST_VALUE){
    // Head pointer: Allocates block of memory from the heap. 
    // Address is return by malloc
    node *head=malloc(sizeof(node));

    // Error handling
    if(head == NULL){
        return(0);
    }
    //////////////////////////
    // Fields initialization//
    //////////////////////////
    // Pointer to the head points to data. 
    head->data = FIRST_VALUE;
    // Node pointer points to next value (NULL)
    head->next = NULL;
    // Returns pointer to head of node
    return head;
}
//____________________________________
// Read a Linked List from a .txt
node* READ_LIST(const char* FILEPATH){
    //////////////////////////////
    // Empty list initialization//
    //////////////////////////////
    // HEAD POINTER
    node *head = NULL;
    // POINTER FOR LAST NODE ADDED
    node *current = NULL;
    // Temporal variable to store values from .txt
    int value; 
    //////////////
    // OPEN FILE//
    //////////////
    // File structure pointer
    FILE *fp;
    // File for reading 
    fp = fopen(FILEPATH, "r"); 
    // Error handling
    if(fp == NULL){
        printf("ERROR: FILE CAN'T BE READ"); 
        return NULL;
    }
    /////////////////////////////
    // CAPTURE VALUES FROM FILE//
    /////////////////////////////
    // Control mechanism to read data sequentially from file
    // fscanf reads numbers from file and stores in address variable location
    while (fscanf(fp, "%d",&value) == 1){
        // Successfully read one integer and stored it in value

        // ADD NEW NODE
        node *new_node = malloc(sizeof(node)); 

        // Error handling
        if(new_node == NULL){
            // Close the file
            fclose(fp);
            return NULL;
        }
        //////////////////////////
        // Fields initialization//
        //////////////////////////
        // Pointer to the head points to data. 
        new_node->data = value;
        // Node pointer points to next value (NULL)
        new_node->next = NULL;

        //////////////////////////////
        // Link new node to the list//
        //////////////////////////////
        // Initial case: List is empty
        if (head == NULL){
            // Head pointer
            head = new_node; 
            // POINTER FOR LAST NODE ADDED
            current = new_node;
        } else {
            // Link current last node to new node
            current->next = new_node;
            // POINTER FOR LAST NODE ADDED
            current = new_node; 
        }
    }
    // Close file
    fclose(fp);
    // Return address of head of list
    return head; 
}
//____________________________________
void WRITE_LIST(node* head, const char* FILEPATH){
    //////////////
    // OPEN FILE//
    //////////////
    // File structure pointer
    FILE *fpW;
    // File for reading 
    fpW = fopen(FILEPATH, "w"); 
    // Error handling
    if(fpW == NULL){
        printf("ERROR: FILE CAN'T BE READ"); 
    }
    /////////////////////////
    // WRITE VALUES TO FILE//
    /////////////////////////
    // Temporal pointer to traverse linked list and write each one on file
    node *current = head;
    while (current!= NULL)
    {
        // Write each data value on file
        fprintf(fpW, "%d\n", current->data);
        // Pointer update
        current = current->next;
    }
    // Close file
    fclose(fpW);
}
//____________________________________
////////////////////////
// 2. PUSH FRONT/BACK //
////////////////////////
int PUSH_FRONT(node** head, int NEW_VALUE){
    // Pointer for new node
    node *node_PUSH_FRONT = malloc(sizeof(node));
    // Error handling
    if (node_PUSH_FRONT == NULL){
        printf("ERROR PUSH FRONT: Unable to allocate enough memory");
        return (1);
    }
    //////////////////////////
    // Fields initialization//
    //////////////////////////
    // Pointer to the node points to data. 
    node_PUSH_FRONT->data = NEW_VALUE;
    // Link new node to currenthead
    node_PUSH_FRONT->next = *head;
    // Updates new head for linked list
    *head = node_PUSH_FRONT;   
    // Return 0 for success
    return (0);
}
//____________________________________
int PUSH_BACK(node* head, int NEW_VALUE){
    // Pointer for new node
    node *node_PUSH_BACK = malloc(sizeof(node));
    // Error handling
    if (node_PUSH_BACK == NULL){
        printf("ERROR PUSH BACK: Unable to allocate memory");
        return(1);
    }
    //////////////////////////
    // Fields initialization//
    //////////////////////////
    // Pointer of the node points to data
    node_PUSH_BACK->data = NEW_VALUE;
    // Updates pointer for next node
    node_PUSH_BACK->next = NULL; 
    /////////////////////////////////////
    // Link new node to the linked list//
    /////////////////////////////////////
    // Case 1: Empty list
    if(head == NULL){
        head = node_PUSH_BACK; 
        return (0);
    }
    // Case 2: List is not empty
    // Pointer to traverse the list
    node *current = head;
    while(current->next != NULL){
        // Update current pointer to next node
        current = current->next;
    }
    // Add new node to end of the list
    current->next = node_PUSH_BACK; 
    // Return 0 for success
    return (0);
}
//____________________________________
///////////////////////
// 3. POP FRONT/BACK //
///////////////////////
int POP_FRONT(node** head){
    // Error handling
    if (*head == NULL){
        printf("ERROR POP FRONT: Unable to POP FRONT node. Empty list");
        return(-1);
    }
    // Pointer to POP node
    node *POP_ADDRESS=*head; 
    // Capture value to POP
    int value_POP=POP_ADDRESS->data;
    // Update head pointer
    *head=POP_ADDRESS->next; 
    // FREE memory for POP node
    free(POP_ADDRESS);
    // Return POP VALUE
    return(value_POP);
}
//____________________________________
int POP_BACK(node** head){
    // Error handling
    if (*head == NULL){
        printf("ERROR POP FRONT: Unable to POP FRONT node. Empty list");
        return(-1);
    }
    ////////////////////////
    // 1. Single node list//
    ////////////////////////
    if((*head)->next==NULL){
        // Capture value
        int value_POP = (*head)->data;
        // FREE memory for POP node
        free(*head);
        // Update head pointer
        *head = NULL; 
        // Return POP value
        return(value_POP); 
    }
    //////////////////////////
    // 2. More than one node//
    //////////////////////////
    // Temporal pointer to traverse linked list second to last
    node* current = *head;
    while (current->next->next!=NULL)
    {
        // Update pointer 
        current = current->next;
    }
    // Current is the second-to-last- last_node is the one to be removed
    node* last_node = current->next;
    // Store the value of last node
    int value_POP = last_node->data;
    //Update the list
    current->next=NULL;
    // FREE memory for POP node
    free(last_node);
    // Return POP VALUE
    return(value_POP);
}
//____________________________________
/////////////////////////////////
// 4. INSERT/REMOVE by position//
/////////////////////////////////
int INSERT_ELEMENT(node** head, int POSITION, int NEW_VALUE){
    ////////////////////
    // CHECH POSITION //
    ////////////////////
    // FRONT
    if (POSITION == 0){
        int NEW_NODE_PUSH_FRONT = PUSH_FRONT(head, NEW_VALUE);
    }
    //////////////////////////
    // Fields initialization//
    //////////////////////////
    // New node
    node *NEW_NODE = malloc(sizeof(node));
    // Error handling
    if(NEW_NODE == NULL){
        printf("ERROR: Unable to allocate new node");
        return 1;
    }
    // Capture value into data
    NEW_NODE->data=NEW_VALUE;
    ///////////////////////
    // Traverse link list//
    ///////////////////////
    // Pointer to traverse link
    node *current = (*head);
    // Counter to traverse link
    int i;
    // Traverse the list
    for (i = 0; i<(POSITION-1);i++){
        // CHECK POSITION: Ensure we havent reach end of the list
        if(current == NULL){
            // FREE allocated memory
            free(NEW_NODE);
            return 1;
        }
        // Point to next node
        current = current->next;
    }
    // CHECK CURRENT POSITION
    if(current == NULL){
        // FREE allocated memory
        free(NEW_NODE);
        return 1;
    }
    ///////////////////
    // NODE INSERTION//
    ///////////////////
    // Perform insertion: New node points to the node after current node
    NEW_NODE->next=current->next;
    // Update current: Points to the new node
    current->next=NEW_NODE;

    return 0;
}
//____________________________________
int REMOVE_ELEMENT(node** head, int POSITION){
    // ERROR HANDLING
    if (*head == NULL) {
        printf("ERROR: Unable to remove element in an empty list");
        return -1;  // Return -1 if the list is empty
    }
    ////////////////////////
    // REMOVAL AT BEGINING//
    ////////////////////////
    if (POSITION == 0) {
        int POP_FRONT_VALUE=POP_FRONT(head);
        printf("The value POP FRONT is %d\n",POP_FRONT_VALUE);
        return 0;
    }
    ///////////////////////
    // Traverse link list//
    ///////////////////////
    // Pointer to hold head pointer 
    node* current = *head;
    // Traverse the list
    for (int i = 0; i < POSITION - 1; i++) {
        if (current->next == NULL) {
            return -1;  // Return -1 if the position is invalid
        }
        current = current->next;
    }
    /////////////////
    // NODE REMOVAL//
    /////////////////
    // Pointer to the next node to free
    node* NODE_TO_FREE = current->next;  // Node to be freed
    // ERROR HANDLING
    if (NODE_TO_FREE == NULL) {
        return -1;  // Return -1 if the position is invalid
    }
    // Capture value to free
    int VALUE_TO_FREE = NODE_TO_FREE->data;  
    // Update current: Points to the node next to the node to be free
    current->next = NODE_TO_FREE->next;  
    free(NODE_TO_FREE);  // Free the memory of the removed node

    return VALUE_TO_FREE;  // Return the value of the removed node
}


////////////////////
// 10. COUNT NODES//
////////////////////
int COUNT_NODES(node *head) {
    // Counter for the number of nodes
    int count = 0;
    // Pointer to hold head pointer position
    node *current = head;
    ///////////////////////
    // Traverse link list//
    ///////////////////////
    while (current != NULL) {
        // Increment the count for the current node
        count++;
        // Update current pointer: Move to the next node in the sequence
        current = current->next;
    }
    // Return count
    return count;
}
//////////////////
// 2. Print list//
//////////////////
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
