from lib import *
from os import getcwd,chdir
from importlib import import_module

tts = tts()
#inp = detection().run()
inp = "what's the time"
print(inp)

chdir("./func")
functions = []
functions = getcwd()
for i in functions:
    function = import_module(i)
    output = function.func(inp, tts)
    if output == True:
        pass
if output == False:
    tts.say("Sorry, i don't have that function")
