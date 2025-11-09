//-------------------------------------------------------------
// Copyright (c) 2011 Matthews Swedot AB.  All rights reserved.
//-------------------------------------------------------------
/// @file bit_stream.hpp

#pragma once

#include <atomic>
#include <stdint.h>
#include <memory>
#include <thread>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cmath>

// Using targeted declarations to avoid namespace pollution
using std::atomic;
using std::min;
using std::cout;
using std::endl;


//========
// BUFFER=
//========
// holds the actual data (packed uint64_t chunks) and manages atomic access.
template <typename T>
class Buffer {
public:
    const int log_size;
    const long capacity;
    // The segment array is now an array of atomic elements for safe concurrent access
    atomic<T> *segment;

    Buffer(int log_size) 
        : log_size(log_size), 
          capacity(1L << log_size),
          segment(new atomic<T>[capacity]) 
    {
        for (long i = 0; i < capacity; ++i) {
            segment[i].store(0);
        }
    }

    ~Buffer() {
        delete[] segment;
    }

    long size() const {
        return capacity;
    }

    // Atomic read operation:
    // Ordering logic is handled by "i"
    // memory_order_relaxed: get a valid value
    T get(long i) const {
        return segment[i & (capacity - 1)].load(std::memory_order_relaxed);
    }

    // Atomic write operation 
    void put(long i, T v) {
        // Relaxed memory ordering for the data write itself
        segment[i & (capacity - 1)].store(v, std::memory_order_relaxed);
    }
};
//_______________________________
//===============================
// Memory management placeholder=
//===============================
// Crucial for safely deleting old buffers.
struct Reclaimer {
    template <typename T>
    void reclaim(Buffer<T>* buffer) {
        if (buffer) {
            // It assumes no other thread is still using 'buffer'.
            delete buffer;
        }
    }
};
//_______________________________
//===========
// BITSTREAM=
//===========
class BitStream {
public:
    // Alias for type of stream 
    typedef long size_type; 

    BitStream() 
        : top(0), 
          bottom(0),
          reclaimer()
    {
        // Initial capacity: 2^log_initial_size = 16 elements (uint64_t)
        // Total bits: 16 * 64 = 1024 bits
        buffer = new Buffer<uint64_t>(log_initial_size);
        unlinked = nullptr;
    }

    ~BitStream() {
        // Clean up the main buffer and any pending unlinked buffer
        delete buffer;
        reclaimer.reclaim(unlinked);
    }
    
    // Returns the current number of available bits in the stream
    size_type size() const {
        return bottom.load(std::memory_order_relaxed) - top.load(std::memory_order_relaxed);
    }

    // Truncates the stream by adjusting the bottom index
    void resize(size_type new_bit_size) {
        // Find the current read position
        long current_top = top.load(std::memory_order_relaxed);
        
        // Calculate the new bottom index based on the new size
        long new_bottom = current_top + new_bit_size;

        // Atomically set the new bottom index.
        bottom.store(new_bottom, std::memory_order_release);
    }
    //==============
    // Write method=
    //==============
    void write(unsigned long value, int bits) {
        long b_start;
        long b_next;
        
        // CAS OPERATION: loop to reserve 'bits' space at the bottom
        do {
            // Use bottom index to write
            b_start = bottom.load(std::memory_order_relaxed);
            b_next = b_start + bits;

            // Get Buffer Address
            long t = top.load(std::memory_order_acquire);
            // Atomic pointer: Local pointer to atomic member
            atomic<Buffer<uint64_t>*>* buffer_ptr = &buffer;
            // CURRENT BUFFER POINTER: load fetches value in atomic pointer
            Buffer<uint64_t> *a = buffer_ptr->load(std::memory_order_relaxed);
            
            //RESIZE CHUNK: Due to buffer use we use the largest integer type
            // Instead of previous 32 bits, with 64 we maximize efficiency
            // MAX capacity of buffer: chunks * 64 bits
            long max_bits = a->size() * 64;
            
            if (b_next - t >= max_bits - 1) {
                // Resize logic: This mimics the deque's buffer expansion
                a = expand(t, b_start, a->log_size + 1);
            }
            
        // Atomically claim the new index range (b_start, b_next)
        // Update bottom to b_next
        } while (!bottom.compare_exchange_weak(b_start, b_next,
                                                std::memory_order_release,
                                                std::memory_order_relaxed));

        // After successful CAS, b_start is the confirmed starting bit index.
        Buffer<uint64_t> *a = buffer.load(std::memory_order_relaxed);

        // Mask to ensure values are placed in MSB first order
        unsigned long current_value_mask = 1UL << (bits - 1);

        //============================
        // Fundamental writing method=
        //============================
        // Same as the original reference: write bit by bit into the reserved indices
        for (int i = 0; i < bits; ++i, current_value_mask >>= 1) {
            // GLOBAL INDEX: Position of bits in sequence
            // Calculate index of the bit being process
            long current_bit_index = b_start + i;
            // Index of the 64 bits chunk
            long element_index = current_bit_index / 64; 
            // Find position (0 to 63) of the bit within 64 bit chunk
            int bit_offset = current_bit_index % 64;

            // Physical array
            // Fetch the current 64-bit chunk from the buffer.
            uint64_t current_chunk = a->get(element_index);
            
            // Insert data into the correct position of the 64 bits chunk
            // mask isolate the next bit from input
            if (value & current_value_mask) {
                // Bit = 1: temporary mask to target bit position
                // Bitwise OR: forces target bit in chunk to 1
                current_chunk |= (1ULL << bit_offset); // Set bit
            } else {
                // Bit = 0: temporary mask to target bit position
                // Bitwise AND: forces target bit in chunk to 0
                current_chunk &= ~(1ULL << bit_offset); // Clear bit
            }
            // Write the updated 64-bit chunk back
            a->put(element_index, current_chunk);
        }
        
        // Clean up logic
        // When buffer grows the old buffer pointer is stored in "unlinked"
        //  Ensures that memory from smaller stream array is handled.
        reclaimer.reclaim(unlinked);
        unlinked = nullptr;
    }

    //=============
    // Read method=
    //=============
    uint32_t read(int bits) {
        
        long t_start;
        long t_next;
        uint32_t v = 0;
        
        // CAS OPERATION(STEAL): loop to reserve 'bits' space from the top
        do {
            // Use top index
            t_start = top.load(std::memory_order_acquire);
            long b = bottom.load(std::memory_order_acquire);
            
            // Read validation: Check if is beyond the end of stream
            if (t_start + bits > b) {
                // Not enough bits available
                return 0; 
            }
            // New top index
            t_next = t_start + bits;
            
        // Atomically claim the index range (t_start, t_next)
        // Advance top pointer to claim range index from t_start up tp t_next
        } while (!top.compare_exchange_strong(t_start, t_next,
                                            std::memory_order_seq_cst,
                                            std::memory_order_relaxed));
        
        // After successful CAS, t_start is the confirmed starting bit index.
        Buffer<uint64_t> *a = buffer.load(std::memory_order_consume);

        // Mask to ensure values are placed in MSB first order
        unsigned long current_mask = 1UL << (bits - 1);
        
        // Loop 2: Read bit by bit from the reserved indices
        for (int i = 0; i < bits; ++i) {
            // GLOBAL INDEX: Position of bits in sequence
            // Calculate index of the bit being process
            long current_bit_index = t_start + i;
            // Index of the 64 bits chunk
            long element_index = current_bit_index / 64; 
            // Find position (0 to 63) of the bit within 64 bit chunk
            int bit_offset = current_bit_index % 64;

            // Physical array
            // Fetch the current 64-bit chunk from the buffer.
            uint64_t chunk = a->get(element_index); 
            
            // Right shift on the chunk AND bitwise: Moves target bit to the LSB( position 0)
            if ((chunk >> bit_offset) & 1ULL) {
                // Bit = 1: sets bit in V. 
                v |= current_mask;
            }
            // Update mask: Ensures extracted bit is correctly placed. 
            current_mask >>= 1;
        }
        return v;
    }

private:
    // Atomic indices for lock-free access
    atomic<long> top;    
    atomic<long> bottom; 
    
    // Dynamic array pointer. Used atomic for safe swap
    atomic<Buffer<uint64_t>*> buffer; 
    
    // Memory cleaning
    // Pointer to buffer that has been replaced by a new, larger buffer during an expansion.
    Buffer<uint64_t> *unlinked;

    // Safety mechanism: prevents "Use After Free" bugs
    Reclaimer reclaimer;
    
    // Initial capacity: 2^log_initial_size = 16 elements (uint64_t)
    // Total bits: 16 * 64 = 1024 bits
    static const int log_initial_size = 4;

    //===================
    // BUFFER EXPLANSION=
    //===================
    // Dynamic resizing
    Buffer<uint64_t>* expand(long t, long b, int log_new_size) {
        // Load old buffer pointer: current memory address of the existing buffer
        Buffer<uint64_t> *old_a = buffer.load(std::memory_order_relaxed);
        
        // Allocate new buffer: using the log_new_size to calculate the new capacity
        Buffer<uint64_t> *new_a = new Buffer<uint64_t>(log_new_size);

        // DATA MIGRATION
        // Index of first 64 bit chunk        
        long start_chunk = t / 64;
        // Index after the last 64-bit chunk containing data
        long end_chunk = (b / 64) + 1;
        
        for (long i = start_chunk; i < end_chunk; ++i) {
            // Read value from old buffer
            uint64_t v = old_a->get(i);
            // Wrtes the 64 bit value into the same index in new buffer
            new_a->put(i, v); 
        }

        // Lock-Free: Atomically swap the new buffer pointer into place
        // Check if current pointer in buffer is equal to old_a-> write new pointer into buffer
        if (buffer.compare_exchange_strong(old_a, new_a)) {
            // Success: old pointer stored in unliked to be reclaim later
            unlinked = old_a; 
            return new_a;
        } else {
            // Failure: new buffer is redundant and must be deleted to prevent memory leak
            delete new_a;
            // Return pointer to buffer
            return buffer.load(std::memory_order_acquire);
        }
    }
};

