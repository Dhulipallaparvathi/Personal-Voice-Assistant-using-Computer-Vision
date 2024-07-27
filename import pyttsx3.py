import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import time
from datetime import datetime

# init pyttsx
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty('voice', voices[1].id)  # 1 for female and 0 for male voice
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()



def wishme():
    hour=int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:" + query + "\n")
    except Exception as e:
        print(e)
        speak("I didnt understand")
        return "None"
    return query

def get_timetable(day):
    if day == 'monday':
        return 'Your Monday timetable is:\n9am - Math\n11am - History\n2pm - Science'
    elif day == 'tuesday':
        return 'Your Tuesday timetable is:\n10am - English\n1pm - Art\n3pm - PE'
    elif day == 'wednesday':
        return 'Your Wednesday timetable is:\n9am - Science\n11am - Math\n2pm - History'
    elif day == 'thursday':
        return 'Your Thursday timetable is:\n10am - PE\n1pm - English\n3pm - Art'
    elif day == 'friday':
        return 'Your Friday timetable is:\n9am - History\n11am - Science\n2pm - English'
    elif day == 'saturday':
        return 'Your Saturday timetable is:\n10am - Math\n1pm - History\n3pm - PE'
    elif day == 'sunday':
        return 'You have no classes on Sunday!'
    else:
        return "Sorry, I don't have a timetable for that day."

def get_day():
    today = datetime.datetime.today().strftime('%A')
    speak(f"Today is {today}.")
    speak("Would you like to know your timetable for today or a different day?")
    day = input().lower()

    if day == "today":
        get_timetable(today.lower())
    elif day == "different day":
        speak("Which day would you like to know your timetable for?")
        day = input().lower()
        get_timetable(day)
    else:
        speak("Sorry, I didn't understand. Please try again.")




if __name__ == '__main__':
    wishme()
    speak("alto assistance activated ")
    speak("How can i help you")
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia ...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'are you' in query:
            speak("I am amigo developed by Jaspreet Singh")
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif 'open github' in query:
            speak("opening github")
            webbrowser.open("github.com")
        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")
        elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("spotify.com")
        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            loc = "C:\\Users\\jaspr\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(loc)
        elif 'play music' in query:
            speak("opening music")
            webbrowser.open("spotify.com")
        elif 'play music' in query:
            speak("opening music")
            webbrowser.open("spotify.com")
        elif 'local disk d' in query:
            speak("opening local disk D")
            webbrowser.open("D://")
        elif 'local disk c' in query:
            speak("opening local disk C")
            webbrowser.open("C://")
        elif 'local disk e' in query:
            speak("opening local disk E")
            webbrowser.open("E://")
        elif 'today date' in query:
            speak("Today date is ")
            now = datetime.now()
            speak(now)
            print(now)
        elif 'Timetable' or 'timetable' or 'time table' or 'open timetable' :
            speak("Opening Timetable")
            webbrowser.open("file:///E:/timetableclass.html")
        elif 'Reminder' or 'reminder' in query:
            speak("What shall I remind you about?")
            text = str(input())
            speak("In how many minutes?")
            local_time = float(input())
            local_time = local_time * 60
            time.sleep(local_time)
            print(text)
            speak(text)
        elif "time table" in text:
           day = text.split()[-1]
           timetable = get_timetable(day)
            speak(timetable)
            print(timetable)
        elif "stop" in text:
        speak("Goodbye!")
        break
        elif 'sleep' in query:
            exit(0)