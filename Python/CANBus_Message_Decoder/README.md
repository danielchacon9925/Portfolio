# CAN Message Decoder System

![CAN Bus](https://img.shields.io/badge/protocol-CAN-brightgreen) ![Python](https://img.shields.io/badge/python-3.7+-blue) ![OOP](https://img.shields.io/badge/OOP-abstract%20class-yellow)

A Python implementation of a CAN bus message decoding system using Object-Oriented Programming principles. This system demonstrates how to process raw CAN messages into human-readable vehicle data.

## Features

- **Base CANMessage class** with abstract `decode()` method
- **Specialized message types**:
  - `SpeedMessage`: Decodes vehicle speed (km/h)
  - `SteeringAngleMessage`: Decodes steering wheel angle (degrees)
- **Message factory** that creates appropriate message objects based on CAN IDs
- **Error handling** for invalid message codes

## Architecture

```mermaid
classDiagram
    class CANMessage {
        <<abstract>>
        +raw_data
        +__init__(raw_data)
        +decode()*
    }
    
    class SpeedMessage {
        +decode(): str
    }
    
    class SteeringAngleMessage {
        +decode(): str
    }
    
    CANMessage <|-- SpeedMessage
    CANMessage <|-- SteeringAngleMessage