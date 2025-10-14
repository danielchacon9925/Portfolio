////////////////
// HEADER FILE//
////////////////

// Before implementing libraries is necessary to implement 
// INCLUDE GUARDS to prevent compilation more than once. 

#ifndef LIBRERIA_H
#define LIBRERIA_H

// Libraries 
#include <stdio.h>
#include <stdlib.h>

// OBJECT: Struct definition 
typedef struct node{
    int data;
    // Pointer type
    struct node* next; 
} node; // ALIAS

////////////////////////
// 1. List generation //
////////////////////////

// Returns a pointer for the head of the node.
node* CREATE_LIST(int FIRST_VALUE);

// Return a pointer for a value to be read.
// Takes a pointer for the memory address as a string
node* READ_LIST(const char* FILEPATH);

// Function to write a linkedlist to the file 
void WRITE_LIST(node* head, const char* FILEPATH);

//////////////////////////
// 2. INSERTIONS by PUSH//
//////////////////////////

// FRONT //
// Double pointer is needed because the pointer of the head change.
// When adding a new value in front of the pointer to the head of the list
// the head pointer must be updated. 
int PUSH_FRONT(node** head, int NEW_VALUE);

// BACK //
// Single pointer is needed because we are sending the new data to the tail
int PUSH_BACK(node* head, int NEW_VALUE);

////////////
// 3. POPs//
////////////

// FRONT //
int POP_FRONT(node** head);

// BACK //
int POP_BACK(node** head);

/////////////////////////////////
// 4. INSERT/REMOVE by position//
/////////////////////////////////

// Insert element at specific position
int INSERT_ELEMENT(node** head, int POSITION, int NEW_VALUE);

// Remove element at specific position
int REMOVE_ELEMENT(node** head, int POSITION);

///////////////////////////////
// 5. GET ELEMENT by position//
///////////////////////////////

// Return de value at specific position
int GET_ELEMENT(node* head, int POSITION, int valid);

//////////////////////
// 6. SORT POSITION//
/////////////////////

// Sort list
void SORT(node* head, char DIRECTION);

//////////////////
// 7. PRINT LIST//
//////////////////

// Print all the list
void PRINT_LIST(node* head);

//////////////////
// 8. CLEAN LIST//
//////////////////

// Free memory
int CLEAN_LIST(node** head);

//////////////////
// 9. COUNT NODES//
///////////////////

// How many node are on a linked list
int COUNT_NODES(node* head);


void print_debug(node* head);

#endif