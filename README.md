# Gate opening system

## Description
This project integrates IoT (Internet of Things) with computer vision for a smart gate system. It involves face recognition using computer vision to control the gate mechanism via an IoT device. The system detects recognized faces and triggers actions on the IoT device, such as opening or closing the gate.

## Requirements

### Hardware Requirements:
- IoT Device (e.g., ESP32, Raspberry Pi Pico)
- Camera module compatible with the IoT device
- Servo motor for gate control
- Computer with webcam for face recognition

### Software Requirements:
- MicroPython firmware for the IoT device
- Python interpreter (version 3.x) for computer vision tasks
- Required Python libraries:
  - `opencv-python`
  - `numpy`
  - `face-recognition`
  - `cvzone`
  - `firebase-admin`
  - `pyserial`

## Setup Instructions

1. **Clone the Repository:**
   - Clone the repository to your local machine using Git:
     ```sh
     git clone https://github.com/your-username/your-repository.git
     ```

2. **Navigate to Project Directory:**
   - Open a terminal and change to the project directory:
     ```sh
     cd your-repository
     ```

3. **Prepare Firebase Credentials:**
   - Obtain the `serviceAccountKey.json` file from your Firebase project settings.
   - Place it in the root directory of the project.

4. **Run Computer Vision Script:**
   - Execute the computer vision script on your computer:
     ```sh
     python cv_gateopening.py
     ```

5. **Run IoT Script:**
   - Flash the MicroPython script `iot_gateopening.py` onto your IoT device (e.g., ESP32, Raspberry Pi Pico).
   - Ensure the IoT device is connected to the same network as your computer.

6. **Verify Functionality:**
   - Upon running the system, verify that face recognition triggers the appropriate actions on the IoT device, controlling the gate mechanism.

## Additional Notes:
- Ensure all paths to files (such as images, Firebase credentials) are correct in the scripts.
- Adjust the UART communication parameters in the IoT script if necessary to match with your hardware setup.

