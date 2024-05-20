# Gate opening system

## Description
This project integrates IoT (Internet of Things) with computer vision for a smart gate system. It involves face recognition using computer vision to control the gate mechanism via an IoT device. The system detects recognized faces and triggers actions on the IoT device, such as opening or closing the gate.

## Requirements

### Hardware Requirements:
- [ ] IoT Device (e.g., ESP32, Raspberry Pi Pico)
- [ ] Camera module compatible with the IoT device
- [ ] Servo motor for gate control
- [ ] Computer with webcam for face recognition

### Software Requirements:
- [ ] MicroPython firmware for the IoT device
- [ ] Python interpreter (version 3.x) for computer vision tasks
- [ ] Required Python libraries:
  - `opencv-python`
  - `numpy`
  - `face-recognition`
  - `cvzone`
  - `firebase-admin`
  - `pyserial`

### Setup Instructions:
1. **Setup IoT Device:**
   - Flash MicroPython firmware onto the IoT device.
   - Upload the provided MicroPython script to the device using a tool like Thonny IDE.

2. **Install Required Libraries:**
   - On the computer, install the necessary Python libraries using pip:
     ```
     pip install opencv-python opencv-python-headless numpy face-recognition cvzone firebase-admin pyserial
     ```

3. **Prepare Firebase Credentials:**
   - Obtain the `serviceAccountKey.json` file from your Firebase project settings.
   - Place it in the same directory as the computer vision script.

4. **Run the Code:**
   - Execute the computer vision script on your computer.
   - Ensure the IoT device is connected to the same network as the computer and is listening for UART commands.

5. **Verify Functionality:**
   - Upon running the system, verify that face recognition triggers the appropriate actions on the IoT device, controlling the gate mechanism.


