// Write a function that takes an integer array and its size
// Returns the sum of its elements using only pointers
#include<stdio.h>
#include<stdlib.h>

int array_sum(int *arr, int size){

    int sum = 0;
    // To solve this pointer oriented is necesary 
    // First "*" define ptr as pointer
    for (int *ptr = arr; ptr < arr + size ; ptr++){
        // "*": Dereferencing: retrieves the value store 
        sum += *ptr;
    }
    return sum;
}

void main(){
    
    int a[] = {10,10,10,10}; 
    int tamaño = sizeof(a)/sizeof(a[0]); 

    printf("La sumatoria del array debe de ser 40: %d\n", array_sum(a, tamaño));
}   