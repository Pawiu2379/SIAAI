#TODO: Voice is not yet implemented

import speech_recognition as sr
from gtts import gTTS
import pygame
import os
import wave
def speak(text):
    tts = gTTS(text=text, lang='en')

    tts.save("output.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()
    pygame.event.wait()

def listen():
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    # Use the microphone as source
    with sr.Microphone() as source:
        audio = recognizer.listen(source,timeout=10)

    try:
        # Recognize speech using Google Speech Recognition
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")


