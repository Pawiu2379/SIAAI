from _datetime import datetime
import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import wikipedia
import pyjokes
import random
import wolframalpha


#speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
activationWord = "computer"
#browser path
browser_path = r"C:\Users\pawel\AppData\Local\Programs\Opera\launcher.exe"
webbrowser.register('opera',None,webbrowser.BackgroundBrowser(browser_path))

def speak(text,rate =120):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def parse_command():
    lisener = sr.Recognizer()
    print("Listening...")
    with sr.Microphone() as source:
        lisener.pause_threshold = 2
        input_speech = lisener.listen(source)
    try:
        print("Recognizing...")
        query = lisener.recognize_google(input_speech, language='en-US')
        print(f"You said: {query}\n")
    except Exception as exeption:
        print('I didn\'t get that. Please try again.')
        speak('I didn\'t get that. Please try again.')
        print(exeption)
        return "None"
    return query

#main
if __name__ == "__main__":
    speak("Hello, What can I help you with?")
    while True:
        query = parse_command().lower().split()
        if query[0] == activationWord:
            query.pop(0)

            #list of commands
            if query[0] == "say":
                if 'hello' in query:
                    speak("hello")
                else:
                    query.pop(0)
                    speech = " ".join(query)
                    speak(speech)

            if query[0] == "open" and query[1] == "browser":
                webbrowser.open_new("https://www.google.com")

            if query[0] == "search" and query[1] == "for" :
                webbrowser.get('opera').open_new(f"https://www.google.com/search?q={query[2]}")



