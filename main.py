from os import listdir, chdir, system
from sys import platform, argv
from importlib.machinery import SourceFileLoader
from time import sleep
from pyttsx3 import init as tts_init
import speech_recognition as sr

###Config Handling###
try:
    import config
except:
    config = open('config.py','w')
    if platform == 'linux' or 'linux2':
        config.write('tts_voice = None\ntts_rate = 125\nsr_mic = None')
    else:
        config.write('tts_voice = None\ntts_rate = 170\nsr_mic = None')
    config.close()

###Library###
class lib:
    # init
    def __init__(self):
        self.args_init()
        self.tts_init()

###Arguments###
    # init
    def args_init(self):
        self.args = argv[:1]
        if self.args_contains('-h','--help'):
            self.debug_enabled = True
            self.args_help()
            exit(0)
        else:
            if self.args_contains('-D','--debug'):
                self.debug_enabled = True
            elif self.args_contains('-n','--normal'):
                self.debug_enabled = False
            else:
                self.debug_enabled = False

    # help
    def args_help(self):
        print('Usage: main.py [argument]')
        print('Arguments:')
        print('-h/--help = help menu (this menu)')
        #print('-d/--daemon = daemon mode (functions running in background)')
        print('-D/--debug = debug mode (no speech recognition)')
        print('-n/--normal = normal mode (speech recognition)')

    # function for checking if argument is specified
    def args_contains(self, short, long):
        if short in self.args or long in self.args:
            return True
        else:
            return False

###Text To Speech###
    # init
    def tts_init(self):
        if platform != 'linux':
            self.tts = tts_init()
            try:
                if config.tts_voice != None:
                    self.tts.setProperty('voice', config.tts_voice)
                self.tts.setProperty('rate', config.tts_rate)
            except:
                pass

    # function for saying
    def say(self, string):
        print('> %s' %(string))
        if self.platform != 'linux':
            self.tts.say(string)
            self.tts.runAndWait()
        elif self.platform == 'linux':
            try:
                if config.tts_voice != None:
                    system('espeak -r %i "%s"' %(config.tts_rate, string))
                else:
                    system('espeak -r %i -v %s "%s"' %(config.tts_rate, config.tts_voice, string))
            except:
                system('espeak -r 125 "%s"' %(string))

###Speech Recognition###
    # init
    def sr_init(self):
        self.sr_r = sr.Recognizer()
        try:
            if config.sr_mic == None:
                self.sr_mic = sr.Microphone()
            else:
                 self.sr_mic = sr.Microphone(device_index=config.sr_mic)
        except:
            self.sr_mic = sr.Microphone()

    # function for configuring what microphone to use
    def sr_config(self):
        print('Available microphones')
        self.sr_mic.list_microphone_names()
        print('')
        print('Type number of microphone you want to use:')
        return str(input('< '))

    # function for running recognition
    def recognize(self):
        print(self.debug_enabled)
        if self.debug_enabled == True:
            return str(input('< '))
            pass
        elif self.debug_enabled == False:
            self.sr_record = self.sr_r.listen(self.sr_mic)
            return self.sr_r.recognize_google(self.sr_record, lang='pl_PL')

###Misc. Functions###
    # easly identifiable platform
    def platform(self):
        if platform == 'win32':
            return 'windows'
        elif platform == 'linux' or platform == 'linux2':
            return 'linux'
        elif platform == 'darwin':
            return 'macos'

###Main###
class main:
    # init
    def __init__(self):
        #if lib.args_contains('-d','--daemon'):
        #    self.daemon()
        #else:
        #    self.func()
        self.func_recognized = lib.recognize()
        self.func()

    # running functions
    def func(self):
        chdir(r'func')
        self.func_availablefuncs = listdir()
        self.func_availablefuncs.remove('__pycache__')
        self.func_availablefuncs = [x.removesuffix('.py') for x in self.func_availablefuncs]
        self.func_current = 0
        for x in self.func_availablefuncs:
            self.func_currentfunc = SourceFileLoader(x,self.func_availablefunc[self.func_current]).load_module()
            self.func_executed = False
            for x in self.func_currentfunc.activators:
                if self.func_recognized == x and self.func_executed == False:
                    for x in self.func_currentfunc.platforms:
                        if x == lib.platform() or x == 'all':
                            self.func_executed = self.func_currentfunc.func(self.func_recognized, lib)
                            self.func_current += 1

    # running daemons
    # To Do
    def daemon(self):
        chdir(r'daemon')
        self.daemon_availabledaemons = listdir()
        self.daemon_availabledaemons.remove('__pycache__')
        self.daemon_availabledaemons = [x.removesuffix('.py') for x in self.daemon_availabledaemons]
        self.daemon_current = 0
        for x in self.daemon_availabledaemons:
            self.daemon_currentdaemon = SourceFileLoader(x,self.daemon_availabledaemons[self.daemon_current]).load_module()
            self.daemon_executed = False
            if lib.recognize() == x and self.daemon_executed == False:
                for x in self.daemon_currentdaemon.platforms:
                    if x == lib.platform():
                        self.daemon_executed = self.daemon_currentdaemon.func(lib.recognize(), lib)
                        self.daemon_current += 1

###Executing###
lib = lib()
main = main()

