#!/bin/python
from time import localtime

def func(inp, tts):
    if inp == "what time is it" or inp == "tell me what time is it" or inp == "what's the time":
        time = localtime()
        tts.say("The time is %s:%s" (time[3], time[4]))
        return True
    
    else:
        return False
