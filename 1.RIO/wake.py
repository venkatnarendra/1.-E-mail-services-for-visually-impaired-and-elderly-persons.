import speech_recognition as sr
import os
import time
import winsound
import pyglet
import time


def command():
        while True:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                        #frequency = 2500  # Set Frequency To 2500 Hertz
                        #duration = 300  # Set Duration To 1000 ms == 1 second
                        #winsound.Beep(frequency, duration)
                        #time.sleep(0.10)
                        filename = 'beep.wav'
                        music = pyglet.media.load(filename, streaming = False)
                        music.play()
                        time.sleep(music.duration)
                                             
                        try:
                                speech = r.listen(source,timeout = 2,phrase_time_limit=2)
                                text = r.recognize_google(speech,key="AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw")
                                ltext = text.lower()
                                if 'wake up' in ltext:
                                        print(ltext)
                                        os.system("main.py")
                                else :
                                        print(ltext)
                                        continue
                                
                        
                        except Exception as e:
                                pass


command()


