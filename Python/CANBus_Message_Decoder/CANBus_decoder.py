# Simulaet CAN message decoder system. Use OOP to define a base class CANMessage
#   and child classes for different messages (SpeedMessage, SteeringAngleMessage)
#   each subclass should implement a method .decode() that decodes raw bytes to meaningful values
#   Also add a message generator that takes a code and the raw_data. 0x001 for Speed, 0x010 for Steering

# Due to each class implemeting a method, is necesary to use abstracmethod
from abc import ABC, abstractmethod

#_____BASE CLASS____
class CANMessage:
    # Object initiation instance
    def __init__(self, raw_data):
        self.raw_data = raw_data
    # Decode method for each class
    @abstractmethod
    def decode(self):
        # Serves as placeholder
        pass

#_____CHILD CLASS 1____
class SpeedMessage(CANMessage):
    def decode(self):
        # We assume the value is on the first value
        return f"Speed: {self.raw_data[0]} km/h"

#_____CHILD CLASS 2____
class SteeringAngleMessage(CANMessage):
    def decode(self):
        # Take the first 2 bytes of raw_data, convert to int(Big-Endian) and add the degree sign
        return f"Speed: {int.from_bytes(self.raw_data[:2],'big')}°"


def message_generator(data_code,raw_data):
    # Speed message
    if data_code == 0x001:
        print("SpeedMessage was chosen\n")
        return SpeedMessage(raw_data)
    elif data_code == 0x010:
        print("SteeringAngleMessage was chosen\n")
        return SteeringAngleMessage(raw_data)
    else:
        raise ValueError(f"The code entered {data_code} is not valid")


#____TEST CODE____

MESSAGE_1_VALID = message_generator(0x001,bytes([80]))
print(f"El mensaje generado 1 es {MESSAGE_1_VALID}")
print(f"El mensaje decoded 1 es {MESSAGE_1_VALID.decode()}")

MESSAGE_2_VALID = message_generator(0x010,bytes([77]))
print(f"El mensaje generado 2 es {MESSAGE_2_VALID}")
print(f"El mensaje decoded 2 es {MESSAGE_2_VALID.decode()}")

MESSAGE_3_NOTVALID = message_generator(0x100,bytes([57]))
print(f"El mensaje generado 3 es {MESSAGE_3_NOTVALID}")


