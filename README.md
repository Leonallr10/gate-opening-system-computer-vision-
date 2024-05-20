# Gte opening system 
## Description

This project leverages computer vision technology to enhance the functionality of a smart gate system. By integrating computer vision algorithms, the system can recognize faces and trigger corresponding actions on the gate mechanism controlled by an IoT device.

## Computer Vision Features

- **Face Recognition:** The core functionality of the system involves detecting and recognizing faces using computer vision techniques.

- **Keyframe Extraction:** The system extracts keyframes from the video feed captured by the camera. These keyframes serve as reference points for face recognition and gate control.

- **Optical Flow Analysis:** Optical flow algorithms are utilized to analyze the movement of objects in the video stream. This analysis helps in tracking the motion of recognized faces and determining the appropriate action to be taken.

- **Image Processing Techniques:** Various image processing techniques such as normalization, histogram equalization, and noise reduction are applied to enhance the quality of captured images. These techniques improve the accuracy of face recognition under different lighting conditions and environmental factors.

- **Feature Detection and Matching:** Feature detection algorithms such as SIFT (Scale-Invariant Feature Transform), SURF (Speeded-Up Robust Features), and ORB (Oriented FAST and Rotated BRIEF) are implemented to identify key points in the images and match them across frames. This aids in robust face recognition and tracking.

## Functionality Overview

The computer vision component of the system continuously analyzes the video feed from the camera. Upon detecting a face, the system compares it with known faces stored in the database. If a match is found, the system triggers the corresponding action on the gate mechanism controlled by the IoT device. For example, upon recognizing an authorized person, the gate is opened, granting access.

## Benefits

- **Enhanced Security:** The integration of computer vision adds an additional layer of security to the gate system by authenticating individuals based on facial recognition.

- **Convenience:** The automated gate control system eliminates the need for manual intervention, providing convenience to users while ensuring secure access.

- **Scalability:** The modular nature of the system allows for scalability, enabling the addition of new features and improvements to meet evolving requirements.

By leveraging computer vision technology, this project aims to create a robust and efficient smart gate system that enhances security and convenience for users.


## Requirements

### Hardware Requirements:
- IoT Device (e.g., ESP32, Raspberry Pi Pico)
- Camera module compatible with the IoT device
- Servo motor for gate control
- Computer with webcam for face recognition

### Software Requirements:
-Libraries to install in Command:​
 `pip install opencv-python opencv-python-headless numpy face-recognition cvzone firebase-admin pyserial`
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

