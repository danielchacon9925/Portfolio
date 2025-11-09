//-------------------------------------------------------------
// Copyright (c) 2011 Matthews Swedot AB.  All rights reserved.
//-------------------------------------------------------------
/// @file bit_stream.hpp

#pragma once

#include <list>
#include <stdint.h>

class OriginalBitStream {
public:
    // Alias for type of stream
    typedef std::list<bool>::size_type size_type;

    // Method to check container empty
    bool empty() const { return m_stream.empty(); }

    // Get number of bits contained
    size_type size() const { return m_stream.size(); }

    //========
    // RESIZE=
    //========
    // if newSize is smaller than current size, bits are removed from the END. 
    void resize(size_type newSize) { m_stream.resize(newSize); }

    // Compares two OriginalBitStream objects by comparing theirs internal bit list
    bool operator==(const OriginalBitStream& other) const
    {
        return m_stream == other.m_stream;
    }

    //========================================================================
    // Writes bits from the OriginalBitStream beginning  to the end of current stream=
    //========================================================================
    void write(OriginalBitStream& other, int bits)
    {
        // Handles transfer of more than 32 bits by breaking then into chunks of 32 bits
        while (bits > 32) {
            // read(32) extracts the chunk from other 
            write(other.read(32), 32);
            bits -= 32;
        }
        // Append 32 chunk to current Stream
        write(other.read(bits), bits);
    }

    //================================================================================
    // Writes entire content of another OriginalBitStream(other) to the end of current stream=
    //================================================================================
    void write(OriginalBitStream& other)
    {
        write(other, other.size());
    }

    //============================
    // Fundamental writing method=
    //============================
    void write(unsigned long value, int bits)
    {
        // Mask to check MSBs in order
        unsigned long mask = 1UL << (bits - 1);

        // In each iteration mask is shifted
        for (int i = 0; i < bits; ++i, mask >>= 1)
            // Checks value & mask for each bit
            m_stream.push_back(value & mask);
    }



    //============================
    // Fundamental reading method=
    //============================
    uint32_t read(int bits)
    {
        // Mask to place bits into MSB position
        unsigned long mask = 1UL << (bits - 1);
        uint32_t v = 0;
        for (int i = 0; i < bits; ++i, mask >>= 1) {
            // Checks bit at the front
            if (m_stream.front())
                // Set bit in V using mask
                v |= mask;
            // Removes bit from front
            m_stream.pop_front();
        }
        return v;
    }

private:
    // Storage
    std::list<bool> m_stream;
};
