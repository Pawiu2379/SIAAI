#TODO: Voice speach working but listen not

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os

def speak(text):
    tts = gTTS(text=text,lang='en')
    tts.save("output.mp3")
    playsound("output.mp3")
    os.remove("output.mp3")
def listen():
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    # Use the microphone as source
    with sr.Microphone() as source:
        audio = recognizer.listen(source,timeout=10)


    try:
        # Recognize speech using Google Speech Recognition
        text = recognizer.recognize_google(audio,language='pl-PL')
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")


