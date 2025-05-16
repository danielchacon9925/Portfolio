# Circular Buffer Memory Manager (C)

![C](https://img.shields.io/badge/Language-C-blue)
![Use-case](https://img.shields.io/badge/Use-Embedded_Systems-green)
![Buffer](https://img.shields.io/badge/Feature-Circular_Buffer-orange)

## Description

This project implements a **circular buffer (ring buffer)** in C, commonly used in **embedded systems** for efficient memory management when reading and writing data continuously.

It provides constant-time `O(1)` operations for pushing and popping elements while wrapping around the buffer to reuse memory efficiently. It's ideal for **UART communication**, **sensor data logging**, and **real-time streaming**.

## Structure

```c
#define BUFFER_SIZE 256

typedef struct {
    uint8_t buffer[BUFFER_SIZE];  // Memory storage
    uint8_t head;                 // Write index
    uint8_t tail;                 // Read index
    uint8_t count;                // Number of elements in the buffer
} Circ_BUFF;
