import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import font
from PIL import ImageTk,Image
import train
import cv2
import numpy as np
def clear():
    uid.delete(0,'end')
    guid.delete(0,'end')
    pswd.delete(0,'end')

def enrollface():
    detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cam = cv2.VideoCapture(0)

    Id =uid.get()
    sampleNum=0
    while(True):
        ret,img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            
            
            #incrementing sample number 
            sampleNum=sampleNum+1
            #saving the captured face in the dataset folder
            cv2.imwrite("dataset/user."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow('frame',img)
        #wait for 100 miliseconds 
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
        # break if the sample number is morethan 20
        elif sampleNum>40:
            break
    cam.release()
    cv2.destroyAllWindows()

def insert():
    euid = uid.get()
    mail = guid.get()
    gpswd = pswd.get()

    if euid.isnumeric():
        with sqlite3.connect("pw.db") as db:
            c = db.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS user(uid NUMBER NOT NULL,mail TEXT NOT NULL,password TEXT NOT NULL);")
        c.execute('INSERT INTO user(uid,mail,password) VALUES(?,?,?);',(euid,mail,gpswd))
        db.commit()
        db.close()
    else:
        print('please try again with valid details\n')


    

    print("the details enterd are: \n"+euid+'\n'+mail+'\n'+gpswd)

def delete_gui():
    def delete():

        print('del working')
        edel= duid.get()
        if edel.isnumeric():
            with sqlite3.connect("pw.db") as db:
                c = db.cursor()
            
            c.execute('DELETE FROM user WHERE uid = ?',[edel])
            db.commit()
            db.close()
            root.destroy()
        else:
            print('please try again with valid details\n')

    
    
    root = Tk()
    root.title('Delete User')
    l1= Label(root,text='UID')
    duid = Entry(root)
    delt =Button(root, text ="Delete user",command = delete)
    l4= Label(root,text='    ')
    l5= Label(root,text='    ')
    l1.grid(row = 0)
    duid.grid(row = 0,column = 1)
    delt.grid(row = 0,column = 3)
    l4.grid(row = 0, column = 4)
    l5.grid(row = 0, column = 2)
    
    root.mainloop()


root = Tk()
root.title('RIO THE HELPER')
root.geometry("1366x690")
root.resizable(0, 0)
root.configure(background="#417558")

background_image = PhotoImage(file="4.gif")

background = Label(root, image=background_image, bd=0)


frame = Frame(root)
frame.pack()

topframe = Frame(root, height = 100, width = 100, bg = '#417558')
topframe.pack( side = TOP, expand = 1, pady = 30, padx = 30)

bottomframe = Frame(root, height = 100, width = 100, bg = '#417558')
bottomframe.pack( side = BOTTOM, expand = 1, pady = 30, padx = 30 )

leftframe = Frame(root, height = 100, width = 100, bg = '#417558')
leftframe.pack( side = LEFT, expand = 1, pady = 30, padx = 30)

rightframe = Frame(root, height = 100, width = 100, bg = '#417558')
rightframe.pack( side = RIGHT, expand = 1, pady = 30, padx = 30 )                

var = StringVar()
appHighlightFont = font.Font(family='Helvetica', size=28, weight='bold')
label = Message(topframe , textvariable=var, relief=FLAT, width = 500, font=appHighlightFont, bg = '#417558' , fg ='#F0F3F4' )

var.set("RIO ")
label.pack()
var = StringVar()
appHighlightFont = font.Font(family='Helvetica', size=24, weight='bold')
label = Message(topframe , textvariable=var, relief=FLAT, width = 1500, font=appHighlightFont, bg = '#417558' , fg ='#F0F3F4'  )

var.set("Voice based e-mail for visually, physically impaired and elderly persons.")
label.pack()

l1= Label(rightframe,text='UID',padx=20,pady=3,height=1,width=20, bg = '#417558' , fg ='#F0F3F4')
uid = Entry(rightframe)
rs =Button(rightframe, text ="Record Sample",command=enrollface, bg = '#417558' , fg ='#F0F3F4', width = 20)
l2= Label(rightframe,text='    G-mail user ID    ',padx=3,pady=3,height=1,width=10, bg = '#417558' , fg ='#F0F3F4')
guid = Entry(rightframe)
l3= Label(rightframe,text='Password',padx=3,pady=3,height=1,width=10, bg = '#417558' , fg ='#F0F3F4')
pswd = Entry(rightframe,show ="*")
clear = Button(rightframe, text ="Clear Fields ",command = clear, bg = '#417558' , fg ='#F0F3F4', width = 20)
enroll =Button(rightframe, text ="Enroll",command = insert, bg = '#417558' , fg ='#F0F3F4', width = 20)
train =Button(rightframe, text ="Train",command= train.trainface, bg = '#417558' , fg ='#F0F3F4', width = 20)
du =Button(rightframe, text ="Delete User",command = delete_gui, bg = '#417558' , fg ='#F0F3F4', width = 20)
mu =Button(rightframe, text ="Modify User Details", bg = '#417558' , fg ='#F0F3F4', width = 20)
la= Label(rightframe,text='    ', bg = '#417558')
lb= Label(rightframe,text='    ', bg = '#417558')
lc= Label(rightframe,text='    ', bg = '#417558')
ld= Label(rightframe,text='    ', bg = '#417558')
le= Label(rightframe,text='    ', bg = '#417558')
lf= Label(rightframe,text='    ', bg = '#417558')
lg= Label(rightframe,text='    ', bg = '#417558')
lh= Label(rightframe,text='    ', bg = '#417558')
l2.grid(row = 0)
guid.grid(row = 0, column = 1)
la.grid(row = 1)
l3.grid(row = 2)
pswd.grid(row = 2, column = 1)
lb.grid(row = 4)
l1.grid(row = 5)
uid.grid(row = 5,column = 1)
lc.grid(row = 6)
rs.grid(row = 7)
train.grid(row = 7, column = 2)
ld.grid(row = 8)
enroll.grid(row = 9)
lg.grid(row = 9, column = 1)
clear.grid(row = 9, column = 2)
le.grid(row = 10)
mu.grid(row = 11)
lh.grid(row = 11, column = 1)
du.grid(row = 11,column = 2)

var = StringVar()
appFont = font.Font(family='Helvetica', size=12)
label = Message(bottomframe , textvariable=var, relief=FLAT, width = 2500, font=appFont,bg = '#417558' , fg ='#F0F3F4')

var.set("RIO is a part of assistive technology by which anyone can be solely accessible Gmail by every indiviual with their voice. It can be used for logging of Gmail,")
label.pack()
var = StringVar()
appFont = font.Font(family='Helvetica', size=12)
label = Message(bottomframe , textvariable=var, relief=FLAT, width = 2500, font=appFont, bg = '#417558' , fg ='#F0F3F4'  )

var.set(" composing of Email, reading out of Email, deleting of Email and logging out of Gmail with voice commands and user can perform actions manually also.")
label.pack()
background.pack()
root.mainloop()
