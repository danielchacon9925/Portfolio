# Simulate communication between devices


#____Object CANBus____
class CANBus:
    def __init__(self):
        # Empty dictionary for device and its callback
        self.devices = {}

    def add_device(self, device_id, callback_function):
        # Add device to dictionary and store the reference 
        self.devices[device_id]=callback_function
        print("Device added succesfully!")
        print(f"The device {device_id} was added with its callback {callback_function}")
    
    def send_message(self, sender_id, receiver_id, message):
        # Send a message to specific device
        if receiver_id in self.devices:
            print(f"Message send to {receiver_id}")
            # The syntaxis is something like: devices[sender](ecu_callback(sender_id,msg))
            # devices[receiber_id]: dictionary access, function call(sender,msg)
            return self.devices[receiver_id](sender_id, message)
        else:
            print("The receiver is not found in the devices dictionaries")

    def broadcast(self, sender_id, message):
        # send a message to all the devices
        # Dictionary comprehension
        return {
            dev_id: callback(sender_id, message)
            for dev_id, callback in self.devices.items()
        }

#____Callback function____
def ecu_callback(sender,msg):
    print(f"ECU received from {sender}:{msg}")
    return  "ACK"

#____Object instance____
bus = CANBus()

#____Add device____
bus.add_device(0x01,ecu_callback)
bus.add_device(0x03,ecu_callback)
bus.add_device(0x04,ecu_callback)
#____Send message____
bus.send_message(0x02,0x01,"RPM?")
#___Broadcast____
bus.broadcast(0x02,"TEST")
#____Print devices___
print("Devices", bus.devices)