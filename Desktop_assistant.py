import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import os
import webbrowser


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

#speak function used to speak user search text.
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# wishme fuction is used to wish Good morning , Good afternoon and good evening.
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good evening")
    speak("I am jarvis!..Please tell me how may i help you")

# takecommand fuction is used to take command from user.
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        #print(e)
        print("say that again please....")
        return "None"
    return query
# sendEmail function is used to send email from user id to another.
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your gmail.com','password')
    server.sendmail('your gmail.com',to,content)
    server.close()

if __name__=='__main__':
   # print("panwar is good")
   wishme()
  # takecommand()
   #speak("panwar is good")
   while True:
       query=takecommand().lower()
       if 'wikipedia' in query:
           speak('Searching wikipedia....')
           query =query.replace('wikipedia',"")
           results=wikipedia.summary(query,sentences=2)
           speak("According to wikipedia")
           print(results)
           speak(results)
       elif 'open youtube' in query:
           webbrowser.open("youtube.com")
       elif 'open google' in query:
           webbrowser.open("google.com")


       elif 'open stackoverflow' in query:
           webbrowser.open("stackoverflow.com")

       elif 'play music' in query:
           music_dir='D:\music'
           songs=os.listdir(music_dir)
           print(songs)
           os.startfile(os.path.join(music_dir,songs[0]))
       elif 'the time' in query:
           strTime=datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"sir,the time is {strTime}")

       elif 'open code' in query:
           codepath="C:\\users\\Pratigya\\AppData\\local\\programs\\Microsoft VS code\\code.exe"
           os.startfile(codepath)
       elif 'thank you' in query:
           speak("your most welocome..thanks for searching")
           print("thanks for searching")
           exit()
       elif 'who are you' in query:
           speak("hello i am jarvis.. i am ready for your help")
       elif 'email to pratigya' in query:
           try:
               speak("what should i say?")
               content=takecommand()
               to="receiver@gmail.com"
               sendEmail(to,content)
               speak("Email has been sent!")
           except Exception as e:
               print(e)
               speak("sorry my friend pratigya. i am not able to send this email")