# CAN Bus Communication Simulator

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)  
![Simulation](https://img.shields.io/badge/Type-Communication_Simulation-green)  
![CAN](https://img.shields.io/badge/Protocol-CANBus-yellow)

## Description  
A lightweight Python simulation of device communication over a virtual **CAN bus**. Devices register with unique IDs and communicate via direct messages or broadcasts using assigned callback functions—ideal for embedded systems prototyping, automotive simulation, or educational purposes.

### Core Components

- `CANBus.add_device(device_id, callback_function)`  
  Registers a device on the bus with a unique ID and a callback function to handle incoming messages.  
  **Returns:** None

- `CANBus.send_message(sender_id, receiver_id, message)`  
  Sends a message from `sender_id` to a specific `receiver_id`. Invokes the receiver's callback function with the sender ID and message.  
  **Returns:** The return value of the receiver’s callback function (e.g., acknowledgment string) or `None` if receiver not found.

- `CANBus.broadcast(sender_id, message)`  
  Sends a message from `sender_id` to **all** registered devices. Invokes each device’s callback function with the sender ID and message.  
  **Returns:** A dictionary mapping each device ID to its callback return value.

### Example Callback Function

```python
def ecu_callback(sender, msg):
    print(f"ECU received from {sender}: {msg}")
    return "ACK"

### Example Usage
```python
bus.add_device(0x01, ecu_callback)
bus.send_message(0x02, 0x01, "RPM?")
bus.broadcast(0x02, "TEST")