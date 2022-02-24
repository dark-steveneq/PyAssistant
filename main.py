from lib import *
from os import listdir,chdir
from importlib.machinery import SourceFileLoader

tts = tts()
inp = detection().run()
print(inp)

chdir(r'func')

funcfiles = listdir()
funcfiles.remove('__pycache__')
functions = [s.removesuffix('.py') for s in funcfiles]
current = 0

for i in functions:
    function = SourceFileLoader(i,funcfiles[current]).load_module()
    output = False
    for i in function.activators:
        if inp == i and output == False:
            output = function.func(inp, tts)
    current += 1
