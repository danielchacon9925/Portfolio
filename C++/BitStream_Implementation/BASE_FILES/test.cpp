// OG INCLUDES
#include "reference.hpp"
#include "reference_ORIGINAL.hpp" // reference to improve
//#include "solution.hpp"
#include <gtest/gtest.h>


//=== NEW IMPLEMENTATION============
#include <chrono>
#include <iostream>
#include <thread>
#include <vector>
#include <numeric>
#include <algorithm>
#include <mutex>

//============
// OPERATIONS=
//============
// Number of write/read operations per thread
const int BATCH_SIZE = 1000000; 

using std::chrono::high_resolution_clock;
using std::chrono::duration_cast;
using std::chrono::milliseconds;

// SINGLE THREAD COMPARISON
template <typename StreamType>
void run_single_threaded_benchmark(const std::string& name) {
    StreamType stream;
    // Force buffer expansion to happen multiple times
    // to measure the overhead of dynamic sizing in both implementations.
    const int total_ops = BATCH_SIZE * 5; 
    //=============
    // Write phase=
    //=============
    auto start_w = high_resolution_clock::now();
    for (int i = 0; i < total_ops; ++i) {
        stream.write(i % 0xFFFF, 16); // Write 16-bit values
    }
    auto end_w = high_resolution_clock::now();
    auto duration_w = duration_cast<milliseconds>(end_w - start_w);
    //============
    // Read phase=
    //============
    auto start_r = high_resolution_clock::now();
    for (int i = 0; i < total_ops; ++i) {
        stream.read(16);
    }
    auto end_r = high_resolution_clock::now();
    auto duration_r = duration_cast<milliseconds>(end_r - start_r);

    //===============
    // PRINT RESULTS=
    //===============
    std::cout << "  " << name << " Total Ops: " << total_ops * 2 << std::endl;
    std::cout << "  " << name << " Write Time: " << duration_w.count() << " ms" << std::endl;
    std::cout << "  " << name << " Read Time: " << duration_r.count() << " ms" << std::endl;
}
// WRITE DATA: Producer workload
template <typename StreamType>
void producer_work(StreamType& stream, int iterations) {
    for (int i = 0; i < iterations; ++i) {
        // Use a unique value based on thread ID for simple testing
        stream.write(i % 0xFFFF, 16); 
    }
}
// READ DATA: Consumer workload
template <typename StreamType>
void consumer_work(StreamType& stream, int iterations) {
    for (int i = 0; i < iterations; ++i) {
        // Read may return 0 if the stream is temporarily empty, which is normal behavior
        // in a non-blocking concurrent queue.
        stream.read(16); 
    }
}
//===============================
// NEW TEST: Compare performance=
//===============================
TEST(PerformanceTest, SingleThreadedComparison) {
    std::cout << "\n--- Single-Threaded Benchmark ---" << std::endl;
    // 1. Original: Baseline performance, high overhead from std::list node allocation/deallocation
    run_single_threaded_benchmark<OriginalBitStream>("Original (std::list)");
    // 2. Improved: Array-based with atomic operations, should be significantly faster
    run_single_threaded_benchmark<BitStream>("Improved (Lock-Free)");
}
//================
// ORIGINAL TESTS=
//================
TEST(BitStreamTest, WriteVaryingLength)
{
    BitStream stream;

    for (int i = 1; i <= 32; i++)
        stream.write(i, i);

    for (int i = 1; i <= 32; i++)
        EXPECT_EQ(stream.read(i), i);
}

TEST(BitStreamTest, AsymetricReadWrite)
{
    BitStream stream;

    stream.write(0xcafe, 16);
    stream.write(0xdead, 16);

    EXPECT_EQ(stream.read(32), 0xcafedead);
}

TEST(BitStreamTest, ReadOrder)
{
    BitStream stream;

    stream.write(0xdeadcafe, 32);

    EXPECT_EQ(stream.read(8), 0xde);
    EXPECT_EQ(stream.read(12), 0xadc);
    EXPECT_EQ(stream.read(4), 0xa);
    EXPECT_EQ(stream.read(8), 0xfe);
}

TEST(BitStreamTest, Resize)
{
    BitStream stream;

    stream.write(0xcafe, 16);
    stream.write(0xbeef, 16);
    stream.resize(16);

    EXPECT_EQ(stream.size(), 16);
    EXPECT_EQ(stream.read(16), 0xcafe);
}

// MAIN with new test
int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}