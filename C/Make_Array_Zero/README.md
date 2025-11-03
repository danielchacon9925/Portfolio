# Array Reduction to Zero (C Implementation)

This project provides a C implementation of a custom algorithm designed to reduce all elements of an integer array to zero through a process of repeated subtraction. The core logic involves finding the lowest non-zero value in the array and subtracting it from all other non-zero elements until the entire array is filled with zeros.

## Core Logic

The primary function, `Make_Array_Zero`, iteratively performs the following steps:

1. **Find Lowest:** Determine the smallest non-zero element currently present in the array.

2. **Subtract:** Subtract this smallest value from every non-zero element in the array.

3. **Count & Repeat:** Increment a counter and repeat the process until the array is completely zeroed out.

The final count represents the number of iterations required to achieve the zero state.

## Files

* `array_reducer.c` (Assuming this is the filename for the provided code)

## Functions Overview

| Function Name | Return Type | Description | 
 | ----- | ----- | ----- | 
| `Find_Lowest` | `int` | Identifies and returns the lowest non-zero integer value in the array. | 
| `IS_ARRAY_ZEROED` | `bool` | Checks the entire array. Returns `true` if all elements are `0`, and `false` otherwise. | 
| `PRINT_ARRAY` | `int` | Utility function to print the current state of the array to the console for visualization. | 
| `Make_Array_Zero` | `int` | The main execution function. It drives the reduction process, prints intermediate steps, and returns the total number of reduction cycles performed. | 

## How to Compile and Run

1. **Save the code:** Save the provided C code into a file named `array_reducer.c`.

2. **Compile using GCC:**
gcc array_reducer.c -o reducer

./reducer


## Example Output

Given the input array: `{1, 5, 0, 3, 5}`

The output will track the reduction process cycle by cycle:

SIZE: 5 
The smallest value found is: 1 
{0,4,0,2,4,} 
The smallest value found left is: 2
{0,2,0,0,2,} 
The smallest value found left is: 2
{0,0,0,0,0,} 
The smallest value found left is: 0

Loop finished! The array is now full of 0s or the break was hit. The amount of iteration until 0 is: 3