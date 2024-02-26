import serial

import time

# Define the COM port of your Bluetooth adapter
serial_port = "COM7"  # Replace 'x' with the actual COM port number

# Create a serial connection
ser = serial.Serial(serial_port, 9600, timeout=1)

try:
    while True:
        data_to_send = input("Enter data to send: ")  # Get user input
        ser.write(data_to_send.encode())  # Send data to HC-05
        time.sleep(20)  # Wait for a second
except KeyboardInterrupt:
    ser.close()  # Close the serial connection on program exit
