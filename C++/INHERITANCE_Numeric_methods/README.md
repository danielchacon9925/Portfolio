# Numerical Methods Project: Newton–Raphson Algorithm (C++ OOP Implementation)

This project implements the **Newton–Raphson method** to approximate the roots (zeros) of nonlinear functions.  
The program demonstrates **Object-Oriented Programming (OOP)** principles in C++, such as **abstraction**, **inheritance**, and **polymorphism**, to create a reusable numerical solver framework.

---

##  Key Concepts and Design

This implementation showcases several fundamental C++ OOP principles:

1. **Abstract Base Class (`METHOD`)**  
   - Declares two **pure virtual functions** (`Solve_Eq()` and `Solve_Dq()`) that define the interface for any mathematical function.  
   - Provides shared methods for printing results and running the **Newton–Raphson iteration**.

2. **Inheritance**  
   - Derived classes (`D_1`, `D_2`, and `D_3`) each represent a unique mathematical function by implementing `Solve_Eq()` and `Solve_Dq()`.

3. **Polymorphism**  
   - The base class algorithm (`Newton_Raphson`) calls the derived class implementations dynamically, allowing the same algorithm to be reused for different equations.

4. **Modular Design**  
   - Code is organized into separate files:  
     - **Header (`.h`)** → Class declarations  
     - **Source (`.cpp`)** → Method definitions  
     - **Main (`main.cpp`)** → Program execution and user interaction

---

##  Project Structure

| File | Description | Role |
| :--- | :--- | :--- |
| `Newton_Raphson_Method.h` | Declares the abstract base class `METHOD` and derived classes `D_1`, `D_2`, `D_3`. Includes virtual methods and shared utilities. | **Header / Interface** |
| `Newton_Raphson_Method.cpp` | Implements all class methods, including the Newton–Raphson algorithm and each specific function definition. | **Implementation** |
| `main.cpp` | Entry point of the program. Handles user input, calls the solver for each function, and prints formatted results. | **Execution** |

---

##  Evaluated Functions

Each derived class represents a different function and its derivative:

| Class | Function \( f(x) \) | Derivative \( f'(x) \) |
| :--- | :--- | :--- |
| `D_1` | \( f(x) = x^3 + 4x^2 - 10 \) | \( f'(x) = 3x^2 + 8x \) |
| `D_2` | \( f(x) = x^2 - 1 \) | \( f'(x) = 2x \) |
| `D_3` | \( f(x) = x^2 + 2x + 1 \) | \( f'(x) = 2x + 2 \) |

---

##  How the Algorithm Works

The **Newton–Raphson** method iteratively approximates the root of a nonlinear equation using the formula:

\[
x_{i+1} = x_i - \frac{f(x_i)}{f'(x_i)}
\]

The process continues until convergence or until the specified tolerance is reached.

---

##  Compilation and Execution

### Requirements

- A modern **C++ compiler** (C++11 or later), e.g. `g++`
- Any IDE such as **Code::Blocks**, **CLion**, or **Visual Studio Code**

### Compilation (Using g++)

To compile all source files together:

```bash
g++ main.cpp Newton_Raphson_Method.cpp -o newton_solver -std=c++11 -lm
