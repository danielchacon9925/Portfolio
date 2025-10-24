# Two Sum Solution (C++ Brute Force $O(n^2)$)

This repository contains an object-oriented C++ solution for the classic Two Sum problem, implemented using the **brute-force nested loop approach** for **$O(n^2)$ time complexity**. The code is structured with a distinct `Solution` class for the core logic and a `TEST` class for executing test cases.

***

## Problem Description

Given an array of integers `nums` and an integer `target`, the goal is to find the indices of the two numbers in the array that add up to the `target`.

* **Assumption:** Every input is guaranteed to have exactly one solution.
* **Constraint:** The same element may not be used twice.
* **Output:** The function returns a `std::vector<int>` containing the two indices.

***

## C++ Implementation Details

The solution uses modern C++ features, replacing C-style memory management with `std::vector` and classes for structure.

### 1. Function Signature

The core logic is within a protected member function of the `Solution` class:

```cpp
protected:
    std::vector<int> twoSum(std::vector<int>& nums, int target)