import pyttsx3
from pyttsx3 import engine 
import datetime
import speech_recognition
import time

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")
    elif hour>=12 and hour<18:
        speak("Good afternoon sir!")
    else:
        speak("good evening sir!") 

    speak("I am Aakash's assistance How may i help u sir ") 

def takeCommand():
    #  it take microphone input and returns 
    r= speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        r.pause_threshold = 1
        query = r.recognize_google(r.listen(source), language='en-US')
        print("user said:", query)
        if query:
            speak("hello sir")
            time.sleep(2)
            speak("What happend Aakash?")
    return query  

if __name__ == "__main__":
    wishMe()
    takeCommand()