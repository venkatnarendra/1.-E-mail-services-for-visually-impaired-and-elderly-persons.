import cv2
import os
import numpy as np
from PIL import Image

def trainface():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector= cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

    def getImagesAndLabels(path):
        imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
        faceSamples=[]
        Ids=[]
        for imagePath in imagePaths:

            if(os.path.split(imagePath)[-1].split(".")[-1]!='jpg'):
                continue
            pilImage=Image.open(imagePath).convert('L')
            imageNp=np.array(pilImage,'uint8')
            Id=int(os.path.split(imagePath)[-1].split(".")[1])
            faces=detector.detectMultiScale(imageNp)
            
            for (x,y,w,h) in faces:
                faceSamples.append(imageNp[y:y+h,x:x+w])
                Ids.append(Id)
                cv2.imshow("training",imageNp)
                cv2.waitKey(10)
        return faceSamples,np.array(Ids)


    faces,Ids = getImagesAndLabels('dataset')
    recognizer.train(faces, Ids)
    recognizer.save('trainer/trainner.yml')
    cv2.destroyAllWindows()
