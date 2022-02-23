#!/bin/python
import pyttsx3
import speech_recognition as sr

class tts:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 135)
        self.engine.setProperty('voice','english')
    
    def say(self, string):
        print(string)
        self.engine.say(string)
        self.engine.runAndWait()

    def getVoices(self):
        self.voices = self.engine.getProperty('voices')
        for voice in self.voices:
            print("Voice:")
            print("ID: %s" %voice.id)
            print("Name: %s" %voice.name)
            print("Age: %s" %voice.age)
            print("Gender: %s" %voice.gender)
            print("Languages Known: %s" %voice.languages)

class detection():
    def run(self):
        self.r = sr.Recognizer()
        self.microphone = sr.Microphone(device_index=9)
        with self.microphone as source:
            return(self.r.recognize_google(self.r.listen(source)))
