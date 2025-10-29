# Adding Two Numbers Represented by Linked Lists in C

This repository contains a C implementation for adding two non-negative integers represented by **singly linked lists**. The digits are stored in reverse order, where each node contains a single digit.

The code includes helper functions for creating random lists, counting nodes, determining allocation size, and printing the list structure.

---

## Core Problem

Given two non-empty linked lists representing two non-negative integers, where the digits are stored in reverse order, return a new linked list representing their sum.

**Example:**
* List 1: `(2 -> 4 -> 3)` represents $342$
* List 2: `(5 -> 6 -> 4)` represents $465$
* Result: `(7 -> 0 -> 8)` represents $807$ (since $342 + 465 = 807$)

---

## Code Overview

The entire implementation is contained within a single C file structure.

### `struct node`

```c
typedef struct node{
    int data;
    struct node *next;
}node;

### Key Functions

| Function | Description |
| :--- | :--- |
| `RANDOM_LIST(int SIZE)` | Creates a new linked list of size `SIZE + 1` with random single-digit data (0-9). |
| `COUNT_NODES(node *head)` | Counts the number of nodes in a given linked list. |
| `ALLOC_SIZE(int L1_COUNT, int L2_COUNT)` | Calculates the maximum number of nodes between L1 and L2, plus one for a potential final carry. |
| `addTwoNumbers(node* L1, node* L2)` | **Core function.** Calculates the sum of the two linked lists, handling carry-over and unequal lengths. |
| `PRINT_LIST(node* head)` | Utility function to print the elements of the list. |