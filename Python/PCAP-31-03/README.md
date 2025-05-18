# Python Certification Practice Questions

This repository contains a collection of 40 Python practice questions and answers aimed at preparing for Python certification exams. The questions cover a wide range of fundamental Python concepts, syntax, and best practices.

## Code Overview

The script (`practice_questions.py`) includes:
- 40 curated Python questions (Q1-Q40) covering essential topics
- Clear answers with explanations for most questions
- Practical code examples demonstrating key concepts
- Comments throughout for better understanding

## Key Topics Covered

1. **Functional Programming**
   - `map()`, `filter()`, and `lambda` functions (Q1, Q18, Q20, Q27)
   - Recursion (Q14, Q23)

2. **Object-Oriented Programming**
   - Class methods and static methods (Q8, Q12)
   - Inheritance (Q17)
   - `self` keyword (Q32)
   - Polymorphism and instance methods (Q33)

3. **File Handling**
   - File modes and operations (Q6, Q11, Q28, Q37, Q39)
   - `seek()` and `tell()` methods (Q6, Q11)

4. **Memory Management**
   - Garbage collection (Q5, Q36, Q38)

5. **Control Flow & Data Structures**
   - Loops and ranges (Q13, Q15, Q19)
   - Dictionary comprehensions (Q4, Q9)
   - Exception handling (Q10, Q22, Q30)

6. **Miscellaneous Core Concepts**
   - Default arguments (Q3, Q7)
   - Boolean operations (Q2)
   - String operations (Q34)
   - Variable arguments (Q31)
   - Command-line arguments (Q24)
   - Iterator protocol (Q30)

## How to Use

1. Clone the repository
2. Run `practice_questions.py` to see all questions and answers
3. Uncomment specific code blocks to test examples
4. Use as a study reference for Python certification exams

## Example Questions

```python
# Q1: How would you use map() to square each element in a list?
print("R1: map(lambda x: x**2, list)")

# Q14: Recursive lambda example
recursive_lambda = (lambda x: x if x == 0 else x + recursive_lambda(x-1))
print("R14:", recursive_lambda(5))  # Outputs 15

# Q28: File modes
print("R28: 'r+' mode allows both reading and writing")