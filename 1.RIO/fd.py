import cv2
import numpy as np
import speak
import time

def fcd():
    faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
    cam=cv2.VideoCapture(0);
    rec=cv2.face.LBPHFaceRecognizer_create();
    rec.read("trainer\\trainner.yml")

    fontface=cv2.FONT_HERSHEY_SIMPLEX
    while(True):
        
        ret,img=cam.read();
        
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=faceDetect.detectMultiScale(gray,1.3,5);
        
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            global id
            id,conf=rec.predict(gray[y:y+h,x:x+w])
            print(id)
            sid = str(id)
            speak.tts('detected ,user '+sid,'en')
            return id
        
        
