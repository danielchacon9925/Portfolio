# Problem Description

Given an array of integers `nums` and an integer `target`, the goal is to find the indices of the two numbers in the array that add up to the `target`.

* **Assumption:** Every input is guaranteed to have exactly one solution.

* **Constraint:** The same element may not be used twice.

* **Output:** The indices can be returned in any order.

# Implementation Details

The solution uses a nested loop structure to check every unique pair of numbers in the array.

## Function Signature
* `nums`: The input array of integers.

* `numsSize`: The size of the input array.

* `target`: The target sum required.

* `returnSize`: A pointer to an integer where the function writes the size of the returned array (always `2`).

## Algorithm

The function employs the **Brute Force** method:

1. It iterates through the array with an outer loop (`i`).

2. It iterates through the remaining elements with an inner loop (`j = i + 1`), ensuring no element is double-counted or paired with itself.

3. If `nums[i] + nums[j]` equals `target`, the indices `i` and `j` are stored in a dynamically allocated array and returned.

4. **Memory Management:** The result array is allocated using `malloc(2 * sizeof(int))`. The function relies on the caller (`main` function/test suite) to free this memory.

## Complexity Analysis

* **Time Complexity:** O(n²) - Due to the nested loops, the algorithm scales quadratically with the number of elements ($n$) in the worst case.

* **Space Complexity:** O(1) - Excluding the space required for the output array (which is O(1) as it always stores 2 integers).

# Building and Running

The provided code is self-contained and includes the function `twoSum` and a `main` function that executes the `TEST_CASES` function.

## Compilation

Assuming your file is named `Two_Sum.c`, use the GNU Compiler Collection (`gcc`) to compile the source code: gcc Two_Sum.c -o two_sum_test

## Execution

Run the generated executable file: ./two_sum_test

# Test Cases

The `TEST_CASES` function runs the following examples and prints the results directly to the console.

## Test Case 1 (Standard Case)

* **Input List:** `[2, 7, 11, 15]`

* **Target:** `9`

* **Expected Output:** `[0, 1]` (Since 2 + 7 = 9)

## Test Case 2 (Non-Sequential Indices)

* **Input List:** `[3, 2, 4]`

* **Target:** `6`

* **Expected Output:** `[1, 2]` (Since 2 + 4 = 6)

## Test Case 3 (Duplicate Numbers)

* **Input List:** `[3, 1, 2, 3]`

* **Target:** `6`

* **Expected Output:** `[0, 3]` (Since 3 + 3 = 6, using different instances of '3')