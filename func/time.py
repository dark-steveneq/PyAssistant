#!/bin/python
from time import localtime
activators = ['która godzinę', 'jaką mamy godzinę', 'którą mamy godzinę']
platforms = ['all']

def func(inp, tts):
    time = localtime()
    lib.say("Teraz jest godzina %s %s" (time[3], time[4]))
    return True
