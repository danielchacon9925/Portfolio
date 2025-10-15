# Daniel Chacón Mora - Code Portfolio  

Welcome to my code portfolio! This repository showcases projects I've developed in C, C++, Python, Assembly, and Verilog. My main areas of expertise include embedded software development and digital design, making this portfolio relevant for roles in Embedded Software Engineering, SoC Design, and Physical Design Engineering.  

## Key Areas of Focus  

- **Embedded Software Development (C, C++, Assembly)**  
  - Low-level programming for microcontrollers and embedded systems.  
  - Device drivers, real-time systems, and hardware-software interaction.  

- **Digital Design & SoC Development (Verilog, FPGA)**  
  - RTL design and simulation for ASIC/FPGA implementations.  
  - Digital logic design, synthesis, and timing analysis.  


## Project Categories  

###  Embedded Systems (C, C++, Assembly)  
**Artimeticos_basicos** – Implementation of nested loops, arrays, and matrix manipulation to perform fundamental arithmetic operations. 
- **Libreria_llamada_main** – Demonstrates the creation of libraries using header and implementation files, along with array generation and pointer manipulation in a main file..  
- **Microcontroladores** – Embedded C code for real-world applications such as a washing machine controller, seismograph simulation, and tombola (bingo spinning wheel) on platforms like Arduino, STM32, and PIC microcontrollers..
- **Circular Buffer Memory Manager** – C implementation of a circular (ring) buffer providing constant-time push/pop operations with wrap-around indexing for efficient embedded memory management.
- **Algorithm_practice** – This C implementation file provides a comprehensive set of functions for managing two distinct data structures: a singly linked list and a dynamically allocated 2D matrix. For the linked list, it includes full CRUD (Create, Read, Update, Delete) functionality with methods like Notes, READ_LIST/WRITE_LIST (file I/O), PUSH_FRONT/PUSH_BACK, POP_FRONT/POP_BACK, INSERT_ELEMENT, REMOVE_ELEMENT, GET_ELEMENT, and list traversal utilities like COUNT_NODES, PRINT_LIST, and a bubble-sort-based SORT. Separately, it includes functions for matrix management, namely CREATE_MATRIX (using calloc for initialization), PRINT_MATRIX, and CLEAN_MATRIX (for memory deallocation), demonstrating best practices for dynamic memory handling with double pointers.

  
### Digital Design & Hardware Acceleration (Verilog)  
- **4bits_shiftregister** – 4-bit shift register with RTL design, DUT, and testbench. Demonstrates circular rotation (left and right) and shift operations (left and right), along with edge-triggered clocking and reset mechanisms.
- **MDIO_transaction_generator** – Verilog-based MDIO (Management Data Input/Output) transaction generator. Includes RTL design for MDIO frame generation, DUT for protocol simulation, and a testbench for validating read/write operations and error handling.   
- **Serial_paralel_converter** – Module for converting serial data streams into parallel outputs. Features RTL design for bit-level synchronization, DUT for functional verification, and a testbench to validate timing and data integrity.
- **UART_Transfer** – A complete UART (Universal Asynchronous Receiver/Transmitter) implementation in Verilog. Includes RTL design for baud rate generation, start/stop bit handling, and data framing, along with a DUT and testbench for simulating full-duplex communication.


#### UVM Verification Environments  
- **4bits_adder**  
  - Complete UVM testbench with:  
    - Transaction class for operand/result modeling  
    - Constrained-random stimulus generator  
    - Coverage-driven verification  
    - Scoreboard for RTL vs. reference model comparison  

- **8bits_RAM**  
  - UVM environment featuring:  
    - Memory access transactions (read/write)  
    - Protocol-aware driver/monitor  
    - Data integrity checks via scoreboard  
    - Functional coverage for address ranges  

- **Combinational_adder**  
  - UVM infrastructure including:  
    - Parameterized transaction items  
    - Automated regression test suite  
    - Assertion-based protocol checking  


### Scripting & Tooling (Python) 
- **ADAS Sensor Data Processor** – Python-based tool for embedded signal processing pipeline for automotive systems. Filters sensor outliers (±3σ) and computes moving averages to smooth noisy measurements from LiDAR/RADAR systems. Demonstrates NumPy-based statistical analysis and real-time data conditioning for safety-critical applications. 
- **CANBus simulation** – Object-oriented Python simulation of a CAN (Controller Area Network) bus system. It models device communication through a central CANBus class that manages device registration and message transmission. Each device registers with a unique ID and a callback function. The send_message method routes messages to specific devices, while broadcast sends to all. Useful for embedded systems, vehicle networking, or callback-based event communication modeling.
- **CANBus decoder** – This Python project implements an object-oriented CAN bus message decoding system with a base abstract class CANMessage and specialized child classes (SpeedMessage, SteeringAngleMessage) that each implement their own decode() method to convert raw byte data into human-readable values (km/h for speed, degrees for steering angle). The system includes a factory function message_generator that routes incoming CAN messages (identified by codes 0x001 for speed and 0x010 for steering) to their appropriate decoder class, demonstrating key OOP principles like abstraction, inheritance, and polymorphism while providing a scalable foundation for adding new message types in automotive applications.
- **FFT_Power_Signal_Analyzer** – Python script for analyzing electrical power signals using the Fast Fourier Transform (FFT). Given a sampled signal and a sampling rate, the tool computes the frequency spectrum, isolates the positive frequencies, and calculates the magnitude of each frequency component. Useful for identifying harmonics, noise, or fundamental frequencies in AC signals. Includes a test case that synthesizes a signal composed of two sinusoids and prints the frequency domain results.
- **PCAP-31-03** – Python-based tool for practice. Contains 40 Python certification practice questions (Q1-Q40) covering core concepts like functional programming (map(), filter(), lambdas), OOP (classes, inheritance, methods), file handling (seek(), modes), memory management (garbage collection), and control flow (loops, exceptions). Each question includes a concise answer with executable code examples and explanations for key topics like recursive functions, dictionary comprehensions, iterator protocols, and variable arguments. Designed as a study aid, the script demonstrates Python best practices through practical examples—from boolean logic and default parameters to context managers (with blocks) and class attributes—making it ideal for certification prep or general Python mastery. Contributors can expand questions or enhance explanations. 
- **Calculadora_Transformadores** – Python-based tool for calculating transformer parameters, such as turns ratio, voltage, and current. Ideal for electrical engineering applications, it provides quick and accurate computations for transformer design and analysis.  
- **Consumo_API_ICE** – Script that interacts with the ICE (Instituto Costarricense de Electricidad) API to fetch and analyze energy consumption data. Useful for monitoring and visualizing energy usage patterns..  
- **GDS_LOGIC_CELLS_EXTRACTER** – Python utility for extracting and analyzing logic cells from GDSII files. Designed for VLSI and digital design workflows, it aids in parsing and processing layout data for integrated circuits  
- **Implementacion_Optimizacion_Benchmarks_OpenLane** – VLSI project using OpenLane to explore the impact of various optimization configurations (synthesis, floorplanning, and placement) on power and area. Python scripts automate the execution of random configurations, extract data, and organize results into DataFrames for analysis. The project also generates GDSII files during signoff for further physical design analysis. 
- **Listas_dataframes** – Advanced data manipulation techniques using lists and Pandas DataFrames. Includes examples of filtering, sorting, and transforming datasets for data analysis tasks.  
- **Microcontroladores** – Dashboard for visualizing and analyzing results from microcontroller simulations and experiments. Provides an intuitive interface to display performance metrics, sensor data, and system behavior for embedded systems projects.. 
- **Perceptron_Predictor** – Perceptron-based machine learning model for binary classification. Demonstrates training, testing, and prediction using a simple neural network..
- **Poliformismo_Agencia_Bancaria** – project showcasing object-oriented programming (OOP) concepts, particularly polymorphism, through a simulated banking agency system. Includes classes for accounts, transactions, and customer management.
- **Simulador_CACHE** – Models cache behavior, including hit/miss rates, replacement policies, and cache hierarchy, for educational and research purposes.    

## How to Use This Repository  

Each project has its own folder with a `README.md` explaining its functionality, setup instructions, and relevant documentation.  

## Contact  

Feel free to connect with me if you have any questions or if you're interested in my work.  

[LinkedIn](www.linkedin.com/in/daniel-chacón-mora-4522851b4) | [Email](dach.9925@gmail.com)

