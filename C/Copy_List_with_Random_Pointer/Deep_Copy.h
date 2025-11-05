// Header

#ifndef DEEP_COPY_H
#define DEEP_COPY_H

// Libraries 
#include <stdio.h>
#include <stdlib.h>
#include <time.h>


// OBJECT
typedef struct node{
    int val;
    struct node *next;
    struct node *random;

}node;

////////////////////////
// 1. List generation //
////////////////////////
node* RANDOM_LIST(int SIZE);
// Returns a pointer for the head of the node.
node* DEEP_COPY_LIST(node* head);

///////////////////
// 2. Print list //
///////////////////
void PRINT_LIST(node* head);

void PRINT_LIST_MATRIX(node *head);

#endif
