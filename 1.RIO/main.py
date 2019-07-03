
import speech_recognition as sr
import webbrowser as  wb
import speak
import run
import time
import valid_command


def command():
        while True:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak.tts('give me command','en')
                    time.sleep(0.10)
                    
                    try:
                        speech = r.listen(source,timeout=2,phrase_time_limit=2)
                        text = r.recognize_google(speech,key="AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw")
                        valid = valid_command.check(text.lower())
                        if valid == 0 :
                                print("wrong command : "+text.lower())
                                speak.tts("unrecognised command ,"+text+", please  wait" ,'en')
                                continue
                        else:
                                return text.lower()
                        
                    except Exception as e:
                            pass

run.gmail()                            
while True:
    
    cmd = command()
    print(cmd)
    if 'log out' in cmd:
        run.logout()
        break
    elif 'compose' in cmd:
        run.compose()
    elif 'close' in cmd:
            run.c_compose()
    elif 'address' in cmd:
        run.toad()
    elif 'subject' in cmd:
        run.subject()
    elif 'message' in cmd:
        run.msg()
    elif 'send' in cmd:
        run.send()
    elif 'attach' in cmd:
        run.attach()
    elif 'inbox' in cmd:
        run.ib()
    elif 'sent mails' in cmd:
        run.sm()
    elif 'delete' in cmd:
        run.delt()
    elif 'search' in cmd:
        run.search()
    elif 'rio close' in cmd:
        run.close_browser()
    elif 'open browser' in cmd:
            run.open_browser()
    elif 'discard draft' in cmd:
            run.discd()
    elif 'read' in cmd:
            run.read()
    elif 'aap' in cmd:
            run.up()
    elif 'down' in cmd:
            run.down()
    elif 'open' in cmd:
            run.open()
    elif 'go back' in cmd:
            run.go_b()
    elif 'new' in cmd:
            run.un()
    elif 'reload' in cmd:
            run.ref()
    else:
        print('unrecognised command')

    
speak.tts('rio is going to sleep mode','en')
