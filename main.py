import os
import pickle

import cvzone
import numpy as np
import cv2
import face_recognition
import serial
import time

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://gate-"
                  "-system-default-rtdb.firebaseio.com/"
})

serial_port = "COM7"
ser = serial.Serial(serial_port, 9600, timeout=1)
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
imgb=cv2.imread('Resources/background.png')

foldermodepath='Resources/Modes'
modepath=os.listdir(foldermodepath)
imgaemodelist =[]
for path in modepath:
    imgaemodelist.append((cv2.imread(os.path.join(foldermodepath,path))))

file=open("encoded.p",'rb')
encodelistknownids= pickle.load(file)
encodelistknown,studentids=encodelistknownids
print(studentids )
while True:
    success, img = cap.read()

    imgs = cv2.resize(img,(0,0),None,0.25,0.25)
    imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)

    facecurframe= face_recognition.face_locations(imgs)
    encodecurframe = face_recognition.face_encodings(imgs,facecurframe)

    imgb[162:162+480,55:55+640]=img
    imgb[44:44 + 633, 808:808 + 414] = imgaemodelist[0]

    for encoface,faceloc in zip(encodecurframe,facecurframe):
        matches= face_recognition.compare_faces(encodelistknown,encoface)
        facedis= face_recognition.face_distance(encodelistknown,encoface)
        print("matches",matches)
        print("facedis",facedis)

        matchindex= np.argmin(facedis)


        if (matches[matchindex] and matches[0]==True) :
            print("known face detected")
            y1,x2,y2,x1=faceloc
            y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
            bbox= 55+x1,162+y1,x2-x1,y2-y1
            imgb= cvzone.cornerRect(imgb,bbox,rt=0)

            data_to_send = "yes" # Get user input
            ser.write(data_to_send.encode())  # Send data to HC-05
            time.sleep(10)
        if (matches[matchindex] and matches[2] == True):
            print("known face detected")
            y1, x2, y2, x1 = faceloc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
            imgb = cvzone.cornerRect(imgb, bbox, rt=0)

            data_to_send = "nes"  # Get user input
            ser.write(data_to_send.encode())  # Send data to HC-05
            time.sleep(10)
        if (matches[matchindex] and matches[1] == True):
            print("known face detected")
            y1, x2, y2, x1 = faceloc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
            imgb = cvzone.cornerRect(imgb, bbox, rt=0)

            data_to_send = "kes"  # Get user input
            ser.write(data_to_send.encode())  # Send data to HC-05
            time.sleep(10)

            # Wait for a second


    #cv2.imshow("webcam", img)
    cv2.imshow("gate camera",imgb)
    cv2.waitKey(1)


