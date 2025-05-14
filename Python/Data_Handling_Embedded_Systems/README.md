# Sensor Data Processor for ADAS Simulation

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![NumPy](https://img.shields.io/badge/NumPy-1.21%2B-orange)
![Embedded](https://img.shields.io/badge/Application-Embedded_Systems-green)

## Description
A robust Python implementation for processing simulated sensor data from **Advanced Driver Assistance Systems (ADAS)**. This pipeline performs real-time signal conditioning to prepare raw sensor measurements for safety-critical automotive applications.

```python
# Example Input/Output
Input:  [(0, 1.23), (1, 1.89), (2, 0.95), ...]  # (timestamp, raw_value)
Output: [(4, 1.42), (5, 1.38), ...]              # (timestamp, filtered_avg)