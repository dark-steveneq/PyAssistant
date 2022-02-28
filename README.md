# Description
Simple voice assistant framework made in Python
# Dependencies
* pyttsx3
* pyaudio
* speechrecognition
* espeak installed, if on Linux
# How to run?
Run main.py
# How to write functions?
Create new script in func folder. You must create aray named 'activators', with commands, that activate your function. Create new function named 'func', witch accept variables 'inp' and 'tts'. 'inp' is recognized text. 'tts' is text-to-speech.
Usage of 'tts': tts.say(str) - say string
