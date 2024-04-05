import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import datetime
import pywhatkit as wk
engine = pyttsx3.init('sapi5')  # Initialize the SAPI5 engine
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate', 150)  
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def wishMe():
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning Semanti")
    elif hour>=12 and hour<18:
        speak("goor afternoon Semanti")
    else:
        speak("good evening")

if __name__== "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'jarvis' in query:
            print("yes mam")
            speak("yes mam")

        elif 'who are you' in query:
            print('My name is jarvis. I am your personal assistant. I can do everything my creator wanted me to do. How may i be of help to you today?')
            speak('My name is jarvis. I am your personal assistant. I can do everything my creator wanted me to do. How may i be of help to you today?')

        elif 'who created you?' in query:
            print('I dont know who created me but i was created using the python language in visual studio code')
            speak('I dont know who created me but i was created using the python language in visual studio code')

        elif 'what is' in query:
            speak('Searching wikipidea...')
            query = query.replace('what is','')
            results = wikipedia.summary(query,sentences=2)
            speak('according to wikipedia')
            print(results)
            speak(results)

        elif 'just open google' in query:
            webbrowser.open('https://www.google.com/')
        
        elif 'open google' in query:
            speak('what should I search?')
            qry=takeCommand().lower()
            webbrowser.open(f"{qry}")
            results = wikipedia.summary(qry,sentences=1)
            speak(results)
        
        elif 'just open youtube' in query:
            webbrowser.open('https://www.youtube.com/')
        
        elif 'search on youtube' in query:
            query=query.replace("search on youtube","")
            webbrowser.open(f"www.youtube.com/results?search_query={query}")
        
        elif 'close browser' in query:
            os.system("taskkill /f /im chrome.exe")

        
        elif 'open notepad' in query:
            npath="C:\Windows\System32\notepad.exe"
            os.startfile("npath")

        elif 'close notepad' in query:
            os.system("taskkill /f /im notepad.exe")