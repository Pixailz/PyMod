#coding:utf-8
#use scan_port 192.168.1.254

##
# Header

import os
import sys

sys.path.append("./modules")
from utils import cs

modules = {}

available_command = [
    "exit",
    "use",
    "help",
    "cls"
]

 #
##


def init_modules():

    try:

        for value in os.listdir("./modules"):

                value = value.replace(".py", "")

                mod = __import__(value)

                modules[value] = mod

    except FileNotFoundError:
        
        print(f"modules folder not found, exiting ..")
        exit()

def printHelp(arg=0):
    
    if arg == 0:
    
        print("list of available command : ")

        for v in available_command:

            print("    ",v)
    
    elif arg == 1:

        print("List of available module")

        for mod in modules:

            print(f"    {mod}")

def contentCheck(content, module_used):

    print(content, module_used)

def loadMod(module, argument=None):
    
    if module == "scan_port": 
        
        scan_port = modules["scan_port"].ScanMachine(target=argument, output="console")

        contentCheck(content=scan_port.getoutPut(), module_used=module)
        
    elif module == "scan_subnet":

        target = modules["scan_subnet"].SubnetScan(argument)

def welcomeMess():
    print("""\
git : https://github.com/Pixailz/PyMod""")

def checkEntry(command, argument=[]):

    if command == "use":

        if len(argument) > 1 and argument[0] in modules:
            
            mod = argument[0]
            arg = "|".join(argument[1:])
            loadMod(module=mod, argument=arg)

        else:
            printHelp(arg=1)

    elif command == "cls":

        cs()

    elif command == "exit":
        
        exit()

    elif command == "help":
        
        printHelp()

    else:

        print("command not found")

def mainLoop():

    init_modules()
    
    cs()
    
    #welcomeMess()
    
    loop = True

    while loop:

        entry = input("Pix@PyMod : ").strip()
        
        if len(entry.split(" ")) == 1:
            hasArgument = False
        else:
            hasArgument = True

        if hasArgument:

            command = entry.split()[0]
            argument = list()

            count = False

            for value in entry.split(" "):

                if count:

                    argument.append(value)

                else:

                    count = True

            checkEntry(command=command, argument=argument)

        else:

            command = entry.split(" ")[0]
            checkEntry(command=command)

mainLoop()
