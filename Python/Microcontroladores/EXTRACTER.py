import serial
from datetime import datetime
import csv

# Open a csv file and set it up to receive comma-delimited input

############
# punch.csv#
############
# logging = open('punch.csv', mode='a', newline='')
#########
# up.csv#
#########
#logging = open('up.csv', mode='a', newline='')
###########
# down.csv#
###########
logging = open('down.csv', mode='a', newline='')
writer = csv.writer(logging, delimiter=",", escapechar=' ', quoting=csv.QUOTE_NONE)

# Open a serial port that is connected to an Arduino
ser = serial.Serial('/dev/ttyACM0')
ser.flushInput()

# Write out a single character encoded in utf-8
ser.write(bytes('x', 'utf-8'))

while True:
    # Read in data from Serial until \n (new line) received
    ser_bytes = ser.readline()

    # Convert received bytes to text format
    decoded_bytes = ser_bytes.strip().decode("utf-8")  # Strip whitespace from both ends

    # If Arduino has sent a string "stop", exit loop
    if decoded_bytes == "stop":
        break

    # Check if decoded_bytes is not empty before writing to CSV
    if decoded_bytes:
        # Write received data to CSV file
        writer.writerow([decoded_bytes])

# Close port and CSV file to exit
ser.close()
logging.close()
print("logging finished")
