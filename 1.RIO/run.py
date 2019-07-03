from gtts import gTTS
import pyglet
import pyglet.media as media
import os
from selenium import webdriver
import speech_recognition as sr
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key,Controller
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
import time
import speak
import fd
import sqlite3
import win32api, win32con
import winsound

#global user_id
#global pswd
#user_id = "fishvenkatn68"
#pswd = "fishfish"
keyboard = Controller()


#speak.tts('opening, firefox browser','en-us')
driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://www.google.co.in')
# close = 0 means browser is closed is false , which means browser is open

#speak.tts('firefox , is, now opend ','en-us')
#driver = None

def tts1(text, lang):
        file = gTTS(text = text, lang = lang)
        filename = 'temp1.mp3'
        file.save(filename)
        
        src=media.load(filename)
        player=media.Player()
        player.queue(src)
        player.play()
        timeout = time.time() + src.duration
        while time.time() < timeout:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                        filename = 'beep.wav'
                        music = pyglet.media.load(filename, streaming = False)
                        music.play()
                        time.sleep(music.duration)
                        try:
                                speech = r.listen(source,phrase_time_limit=4)
                                text = r.recognize_google(speech)
                                c = text.lower()
                                if 'stop' in c:
                                        player.pause()
                                        player.next()
                                        return
                                else:
                                        continue
                        except Exception as e:
                                pass
        player.pause()
        player.next()
        return
        
        
        

def gmail():
        #authentication part:
	speak.tts("verify ,your self",'en-us')
	uid = fd.fcd()
	with sqlite3.connect("pw.db") as db:
		c = db.cursor()
	c.execute("SELECT mail FROM 'user' WHERE uid = (?);",[uid])
	user_id = c.fetchone()[0]
	c.execute("SELECT password FROM 'user' WHERE uid = (?);",[uid])
	pswd = c.fetchone()[0]
	db.commit()
	db.close()

	speak.tts('signing in gmail','en-us')
	#driver = webdriver.Firefox()
	driver.get('https://accounts.google.com/signin')
	time.sleep(2)
	
	email_id = driver.find_element_by_id("identifierId")
	email_id.send_keys(user_id + Keys.ENTER)
	time.sleep(2)
	pswdi = driver.find_element_by_name('password')
	pswdi.send_keys(pswd + Keys.ENTER)
	time.sleep(2)
	driver.get('https://mail.google.com/mail/#inbox')
	speak.tts('gmail login, successfull','en-us')
	
	return
def login():
   
                gmail()

def logout():
	
	speak.tts('ok,signing out gmail','en-us')
	driver.get("https://mail.google.com/mail/?logout")
	time.sleep(1)
	speak.tts('gmail logout,successfull','en-us')
	driver.close()
	time.sleep(2)
	return

def compose():
	#driver = webdriver.Firefox()
	speak.tts('ok, clicking on compose','en-us')
	#
	add =driver.find_element_by_class_name("z0")
	add.click()
	speak.tts('now you can compose new mail','en')
	return
def c_compose():
	#driver = webdriver.Firefox()
	speak.tts('ok, closing compose mail','en-us')
	keyboard.press(Key.esc)
	keyboard.release(Key.esc)
	speak.tts('compose closed','en-us')
	return

def toad():
                win32api.SetCursorPos((900,315))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,200,200,0,0)
                try:
                        speak.tts('enter senders address','en-us')
                        while True:
                                r = sr.Recognizer()
                                with sr.Microphone() as source:
                                        try:
                                                speak.tts('listening','en-us')
                                                speech = r.listen(source,timeout=2,phrase_time_limit=2)
                                                text = r.recognize_google(speech,key="AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw")

                                                word = text.lower()
                                                if word =='done':
                                                        return
                                                if word == 'back':
                                                        keyboard.press(Key.backspace)
                                                        keyboard.release(Key.backspace)
                                                        continue
                                                if word in ['at the rate gmail dot com','at the rate gmail dot kom','@gmail.com','at the rate gmail.com']:
                                                        word ='@gmail.com'
                                                if word =='space':
                                                        keyboard.press(Key.space)
                                                        keyboard.release(Key.space)
                                                        continue
                                                if word == 'enter':
                                                        keyboard.press(Key.enter)
                                                        keyboard.release(Key.enter)
                                                        continue
                                                if word == 'down':
                                                        keyboard.press(Key.down)
                                                        keyboard.release(Key.down)
                                                        continue
                                                if word == 'aap':
                                                        keyboard.press(Key.up)
                                                        keyboard.release(Key.up)
                                                        continue
                                                add =driver.find_element_by_class_name("vO")
                                                add.send_keys(word)
                                                speak.tts(word+', ok','en-us')
                                        except Exception as e:
                                                pass
                except Exception as e:
                        add =driver.find_element_by_class_name("vO")
                        driver.execute_script("return arguments[0].click();", add)
                        speak.tts('enter senders address','en-us')
                        while True:
                                r = sr.Recognizer()
                                with sr.Microphone() as source:
                                        try:
                                                speak.tts('listening','en-us')
                                                speech = r.listen(source,timeout=2,phrase_time_limit=2)
                                                text = r.recognize_google(speech,key="AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw")

                                                word = text.lower()
                                                if word =='done':
                                                        return
                                                if word == 'back':
                                                        keyboard.press(Key.backspace)
                                                        keyboard.release(Key.backspace)
                                                        continue
                                                if word in ['at the rate gmail dot com','at the rate gmail dot kom','@gmail.com','at the rate gmail.com']:
                                                        word ='@gmail.com'
                                                if word =='space':
                                                        keyboard.press(Key.space)
                                                        keyboard.release(Key.space)
                                                        continue
                                                if word == 'enter':
                                                        keyboard.press(Key.enter)
                                                        keyboard.release(Key.enter)
                                                        continue
                                                if word == 'down':
                                                        keyboard.press(Key.down)
                                                        keyboard.release(Key.down)
                                                        continue
                                                if word == 'aap':
                                                        keyboard.press(Key.up)
                                                        keyboard.release(Key.up)
                                                        continue
                                                add =driver.find_element_by_class_name("vO")
                                                add.send_keys(word)
                                                speak.tts(word+', ok','en-us')
                                        except Exception as e:
                                                pass
                
			
			
			


def subject():
                add = driver.find_element_by_class_name("aoT")
                add.click()
                speak.tts('enter ,subject','en-us')
                while True:
                        
                        
                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                                
                                try:
                                        speak.tts('listening','en-us')
                                        speech = r.listen(source,timeout=2,phrase_time_limit=5)
                                        text = r.recognize_google(speech,key="AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw")
                                        word = text.lower()
                                   
                                        if word =='done':
                                                return
                                        if word =='back':
                                                keyboard.press(Key.backspace)
                                                continue
                                        if word =='space':
                                                keyboard.press(Key.space)
                                                continue
                                        add = driver.find_element_by_class_name("aoT")
                                        add.send_keys(word)
                                   # time.sleep(1)
                                        #keyboard.press(Key.backspace)
                                        speak.tts(word+', ok','en')
                                except Exception as e:
                                        pass

def msg():
                add = driver.find_element_by_css_selector("div[aria-label='Message Body']")
                add.click()
                speak.tts('dictate, your mail','en-us')
                while True:
                        
                        
                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                                
                                try:
                                        speak.tts('listening','en-us')
                                        speech = r.listen(source,timeout=2,phrase_time_limit=10)
                                        text = r.recognize_google(speech,key="AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw")
                                        word = text.lower()
                                   
                                        if word =='done':
                                                return
                                        if word in['back']:
                                                keyboard.press(Key.backspace)
                                                keyboard.release(Key.backspace)
                                                continue
                                        if word =='space':
                                                keyboard.press(Key.space)
                                                keyboard.release(Key.space)
                                                continue
                                        if word =='newline':
                                                keyboard.press(Key.enter)
                                                keyboard.release(Key.enter)
                                                continue
                                        if word == 'tab':
                                                keyboard.press(Key.tab)
                                                keyboard.release(Key.tab)
                                        add = driver.find_element_by_css_selector("div[aria-label='Message Body']")
                                        add.send_keys(word)
                                   # time.sleep(1)
                                        #keyboard.press(Key.backspace)
                                        speak.tts(word+', ok','en-us')
                                except Exception as e:
                                        pass

def send():

        
        msg = driver.find_element_by_css_selector(".Ar.Au")
        msg.click()
        speak.tts('ok , clicking send button','en-us')
        keyboard.press(Key.ctrl)
        keyboard.press(Key.enter)
        keyboard.release(Key.ctrl)
        keyboard.release(Key.enter)
        speak.tts('message sent','en-us')
        return

def ib():
	#driver = webdriver.Firefox()
	speak.tts('ok,opening inbox','en')
	driver.get('https://mail.google.com/mail/#inbox/')
	speak.tts('inbox opend','en')
	return
def read():
        sub = driver.find_element_by_class_name("hP")
        speak.tts("subject, ," + sub.text,"en")
        frm = driver.find_element_by_class_name("gD")
        speak.tts("from, ," + frm.text,"en-us")
        date = driver.find_element_by_class_name("g3")
        speak.tts("recieved,on," + date.text,"en-us")
        msg = driver.find_element_by_css_selector(".ii.gt")
        print('word length '+ str(len(msg.text)))
        if len(msg.text) == 0:
                speak.tts('nothing to read in message section','en-us')
        else:
                speak.tts("wait, rio isfetching the message to read",'en')
                tts1("message,"+ msg.text,"en-us")
                os.remove('temp1.mp3')

def un():
        unread = driver.find_element_by_css_selector(".J-Ke.n0")
        #speak.tts('you have,'+ unread.text+'unread mails','en-us')
        num = unread.text
        c = num[6:-1]
        speak.tts('you have,'+ c +',unread mails','en-us')
        umail = driver.find_element_by_xpath("//*[@class='zF']")
        speak.tts("opening ,unread, mail",'en-us')
        driver.execute_script("return arguments[0].click();", umail)
        speak.tts("opened ,mail",'en-us')
        
        
        

def sm():
	speak.tts('ok,opening inbox','en')
	driver.get('https://mail.google.com/mail/#sent/')
	speak.tts('inbox opend','en')
	return

def delt():
        
        
	dlt = driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div[3]")
	speak.tts('ok, deleting mail','en-us')
	time.sleep(2)
	dlt.click()
	speak.tts('mail deleted','en-us')
	return

def search():
                add =driver.find_element_by_class_name("gbqfif")
                add.click()
                speak.tts('ok ,what do you want to search','en-us')
                r = sr.Recognizer()
                with sr.Microphone() as source:
                        try:
                                speak.tts('listening','en')
                                speech = r.listen(source,timeout=2,phrase_time_limit=5)
                                text = r.recognize_google(speech,key="AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw")
                                word = text.lower()
                                add =driver.find_element_by_class_name("gbqfif")
                                add.send_keys(word+ Keys.ENTER)
                                speak.tts(word+', search done','en-us')
                        except Exception as e:
                                pass
def up():
        
        
	speak.tts('ok','en')
	win32api.SetCursorPos((200,200))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,200,200,0,0)
	#driver.maximize_window()
	#move = driver.find_element_by_css_selector(".gb_Xa.gb_dc")
	#time.sleep(2)
	#move.click()
	keyboard.press(Key.up)
	keyboard.release(Key.up)
	return
def down():
        
        
	speak.tts('ok','en')
	win32api.SetCursorPos((200,200))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,200,200,0,0)
	#driver.maximize_window()
	#move = driver.find_element_by_css_selector(".gb_Xa.gb_dc")
	#time.sleep(2)
	#move.click()
	keyboard.press(Key.down)
	keyboard.release(Key.down)
	return
def open():
	speak.tts('ok','en-us')
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	return
def go_b():
        speak.tts('ok','en-us')
        gb = driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div")
        time.sleep(2)
        gb.click()
        return
        
def discd():
	speak.tts('ok, discarding draft','en-us')
	add =driver.find_element_by_css_selector(".og")
	add.click()
	speak.tts('ok, discarded draft','en-us')

def attach():
        speak.tts('ok, clicking on attach','en-us')
        unread = driver.find_element_by_css_selector(".wG.J-Z-I")
        unread.click()
        speak.tts('attach window opened','en-us')
        win32api.SetCursorPos((180,200))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,180,200,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,180,200,0,0)
        while True:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                        try:
                                speak.tts('listening','en-us')
                                speech = r.listen(source,timeout=2,phrase_time_limit=2)
                                text = r.recognize_google(speech,key="AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw")
                                word = text.lower()
                                if word == 'open':
                                        print(word)
                                        keyboard.press(Key.enter)
                                        keyboard.release(Key.enter)
                                        continue
                                if word == 'attach':
                                        print(word)
                                        keyboard.press(Key.enter)
                                        keyboard.release(Key.enter)
                                        return
                                if word == 'down':
                                        print(word)
                                        keyboard.press(Key.down)
                                        keyboard.release(Key.down)
                                        continue
                                if word == 'aap':
                                        print(word)
                                        keyboard.press(Key.up)
                                        keyboard.release(Key.up)
                                        continue
                                if word == 'left':
                                        print(word)
                                        keyboard.press(Key.left)
                                        keyboard.release(Key.left)
                                        continue
                                if word == 'right':
                                        print(word)
                                        keyboard.press(Key.right)
                                        keyboard.release(Key.right)
                                        continue
                                if word =='back':
                                        keyboard.press(Key.backspace)
                                        keyboard.release(Key.backspace)
                                        continue
                        except Exception as e:
                                pass

def ref():
        driver.execute_script("location.reload()")
        return

		
	

	


