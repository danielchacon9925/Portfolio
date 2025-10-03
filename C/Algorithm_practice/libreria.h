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

/////////////////////
// List generation //
/////////////////////

// Returns a pointer for the head of the node.
node* CREATE_LIST(int FIRTS_VALUE);

// Return a pointer for a value to be read.
// Takes a pointer for the memory address as a string
node* READ_LIST(const char* FILEPATH);

// Function to write a linkedlist to the file 
void WRITE_LIST(node* head, const char* FILEPATH);

///////////////////////
// INSERTIONS by PUSH//
///////////////////////

// FRONT //
// Double pointer is needed because the pointer of the head change.
// When adding a new value in front of the pointer to the head of the list
// the head pointer must be updated. 
int PUSH_FRONT(node** head, int NEW_VALUE);

// BACK //
// Single pointer is needed because we are sending the new data to the tail
int PUSH_BACK(node* head, int NEW_VALUE);

//////////////////////////////
// INSERT/REMOVE by position//
//////////////////////////////

// Insert element at specific position
int INSERT_ELEMENT(node** head, int POSITION, int NEW_VALUE);

// Remove element at specific position
int REMOVE_ELEMENT(node** head, int POSITION);