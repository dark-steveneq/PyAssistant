# Description
Simple voice assistant framework made in Python
# Dependencies
* pyttsx3
* pyaudio
* speechrecognition
* espeak, if using Linux
# How to run?
Run main.py without any arguments if you want to use it like normal voice assistant.
You can use -d parameter to run PyAsistant in daemon mode (To Do).
To configure what voice to use for TTS, rate of voice and may other things, use -c parameter (To Do).
If you're writing functions, I recomend using -D parameter, it will replace voice recognition with input prompt.
To list all available arguments, use -h argument
# How to write functions?
Create new script in func folder. You must create two arays: first named 'activators', witch will include commands, that activate your function and platforms, to check on what platform function can be ran. Valid platforms are: 'windows', 'linux', 'macos' and 'all'. After that, define new function named 'func'. It must accept parameter 'inp' and 'lib'. 'inp' is recognized text, and 'lib' is library class. There are two main function usefull for creating functions:
* lib.say(string) = says provided string with TTS
* lib.recognize() = runs voice recognition and returns recognized text
