cmake_minimum_required(VERSION 3.25)

project(interview)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(GTest REQUIRED)
enable_testing()

add_executable(bit_stream_test test.cpp)
target_link_libraries(bit_stream_test GTest::Main)

include(GoogleTest)
gtest_discover_tests(bit_stream_test)
