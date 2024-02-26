import os

import cv2
import face_recognition
import pickle


foldermodepath='Images'
modepathlist=os.listdir(foldermodepath)
imglist =[]
studentids=[]
for path in modepathlist:
    imglist.append((cv2.imread(os.path.join(foldermodepath,path))))
    studentids.append(os.path.splitext(path)[0])
print(len(imglist))

def findEncoding(imagelist):
    encodelist=[]
    for img in imagelist:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist

encodelistknown=findEncoding(imglist)
encodelistknownids=[encodelistknown,studentids]
print("encoding complete")

file=open("encoded.p",'wb')
pickle.dump(encodelistknownids,file)
file.close()
print("done")