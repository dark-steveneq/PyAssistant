from lib import *
from os import listdir,chdir
from importlib.machinery import SourceFileLoader

tts = tts()
#inp = detection().run()
inp = "test"
print(inp)

chdir(r"func")

files = listdir()
funcfiles = [s.removeprefix("__pycache__") for s in files]
functions = [s.removesuffix(".py") for s in funcfiles]
current = 0

for i in functions:
    function = SourceFileLoader(i,funcfiles[current]).load_module()
    output = False
    for i in function.activators:
        if inp == i:
            output = function.func(inp, tts)
    if output == True:
        pass        
    current += 1
if output == False:
    tts.say("Sorry, i don't have that function")
