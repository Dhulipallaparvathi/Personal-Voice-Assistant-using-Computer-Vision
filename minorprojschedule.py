import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
import time
from datetime import datetime

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception:", str(e))

    return said.lower()

def get_timetable(day):
    if day == 'monday':
        return 'Your Monday timetable is:\n9am - BIO INFORMATICS\n11am - JAVA\n2pm - DBMS'
    elif day == 'tuesday':
        return 'Your Tuesday timetable is:\n10am - JAVA\n1pm - DBMS\n3pm - BIO INFORMATICS'
    elif day == 'wednesday':
        return 'Your Wednesday timetable is:\n9am - CODING\n11am - DAA\n2pm - DBMS'
    elif day == 'thursday':
        return 'Your Thursday timetable is:\n10am - Java\n1pm - BIO INFORMATICS\n3pm - DAA'
    elif day == 'friday':
        return 'Your Friday timetable is:\n9am - BIO INFORMATICS\n11am - DAA\n2pm - JAVA'
    elif day == 'saturday':
        return 'Your Saturday timetable is:\n10am - BIO INFORMATICS\n1pm - DAA\n3pm - CODING'
    elif day == 'sunday':
        return 'You have no classes on Sunday!'
    else:
        return "Sorry, I don't have a timetable for that day."
        
while True:
    print("How can I assist you?")
    speak("How can I assist you?")
    text = get_audio()

    if "time table" in text:
        day = text.split()[-1]
        timetable = get_timetable(day)
        speak(timetable)
        print(timetable)
    elif "stop" in text:
        speak("Goodbye!")
        break
