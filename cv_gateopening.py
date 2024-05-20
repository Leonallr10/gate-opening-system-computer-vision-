import cv2
import numpy as np
import face_recognition
import pickle
import os
import serial
import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://gate-system-default-rtdb.firebaseio.com/"
})

# Serial port for UART communication
serial_port = "COM7"
ser = serial.Serial(serial_port, 115200, timeout=1)
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
imgb = cv2.imread('Resources/background.png')

# Load mode images
foldermodepath = 'Resources/Modes'
modepath = os.listdir(foldermodepath)
imgaemodelist = [cv2.imread(os.path.join(foldermodepath, path)) for path in modepath]

# Load encoded faces
with open("encoded.p", 'rb') as file:
    encodelistknown, studentids = pickle.load(file)

print(studentids)

# Function to apply image processing techniques
def preprocess_image(img):
    # Normalize the image
    img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)
    # Apply histogram equalization
    img = cv2.equalizeHist(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
    # Reduce noise
    img = cv2.GaussianBlur(img, (5, 5), 0)
    return img

# Feature detection and matching function
def detect_and_match_features(img, encodelistknown):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sift = cv2.SIFT_create()
    kp, des = sift.detectAndCompute(gray, None)
    matches = []
    for known_des in encodelistknown:
        bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
        matches.append(bf.match(des, known_des))
    return matches

# Keyframe extraction and optical flow
def extract_keyframes_and_optical_flow(cap):
    ret, prev_frame = cap.read()
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    keyframes = []
    optical_flows = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        flow = cv2.calcOpticalFlowFarneback(prev_gray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        keyframes.append(frame)
        optical_flows.append(flow)
        prev_gray = gray
    return keyframes, optical_flows

while True:
    success, img = cap.read()
    if not success:
        break

    img = preprocess_image(img)
    matches = detect_and_match_features(img, encodelistknown)
    if matches:
        for match in matches:
            if len(match) > 0:
                print("known face detected")
                ser.write(b"yes")  # Send data to UART
                time.sleep(10)
                break

    cv2.imshow("gate camera", img)
    cv2.waitKey(1)

