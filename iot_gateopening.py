from machine import UART, Pin, PWM
import time
import network
import urequests

# WiFi and Firebase credentials
ssid = "R18"
passwd = "rpi12345"
firebase_url = 'https://espcam-68e80-default-rtdb.firebaseio.com/test.json'
auth_data = {
    "email": "firebaseburner0@gmail.com",
    "password": "firefirebasebase",
    "returnSecureToken": True
}

# Initialize UART
uart = UART(0, baudrate=115200, tx=0, rx=1)

# Connect to WiFi
def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, passwd)
    while not wlan.isconnected():
        print('Waiting for connection...')
        time.sleep(1)
    print(wlan.ifconfig())

try:
    connect()
except KeyboardInterrupt:
    machine.reset()

# Authenticate to Firebase
auth_response = urequests.post(
    "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyC23aNFU8tzgb0hOFtT1OX7V1DlntQFx7M",
    json=auth_data
)
auth_response_data = auth_response.json()
auth_response.close()
local_id = auth_response_data.get('localId')

# Function to get the next key for Firebase
def get_next_key():
    try:
        response = urequests.get(firebase_url)
        data = response.json()
        response.close()
        if not data:
            return "t1"
        keys = [key for key in data.keys() if key.startswith('t')]
        keys.sort(key=lambda x: int(x[1:]))  # Sort keys numerically
        last_key = keys[-1]
        last_number = int(last_key[1:])  # Extract the integer part of the last key
        return f"t{last_number + 1}"
    except Exception as e:
        print(f"Error getting next key: {e}")
        return "t1"

# Function to handle servo movement
def handle_servo():
    servo = PWM(Pin(10))  # the Pico PWM pin
    servo.freq(50)
    
    # Move to 150 degrees
    servo.duty_u16(7500)
    time.sleep(0.9)  # Wait for the servo to move
    servo.deinit()
    time.sleep(3)
    
    # Return to normal position
    servo.duty_u16(3500)
    time.sleep(0.8)  # Wait for the servo to move
    servo.deinit()

# Main loop to handle UART communication and Firebase logging
while True:
    if uart.any():
        data = uart.readline().decode().strip()  # Read data from UART
        print("Received:", data)
        if data in ["yes", "nes", "kes"]:
            handle_servo()
            
            current_time = time.time()
            local_time = time.localtime(current_time)
            time_string = "{:02d}:{:02d}:{:02d}".format(local_time[3], local_time[4], local_time[5])
            date_string = "{:02d}-{:02d}-{:02d}".format(local_time[2], local_time[1], local_time[0])            
            
            next_key = get_next_key()
            data_to_send = {
                next_key: {
                    "time": time_string,
                    "date": date_string
                }
            }
            
            response = urequests.patch(firebase_url, json=data_to_send)
            response_data = response.json()
            response.close()
            print(response_data)
    time.sleep(1)  # Delay for stability
