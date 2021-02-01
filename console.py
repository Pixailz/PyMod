#coding:utf-8

import importlib
import sys
sys.path.append("./modules")
import os

modules = []

available_command = [
    "exit",
    "use",
    "help",
    "cls"
]

def init():

    try:

        for v in os.listdir("./modules"):

            modules.append(v.replace(".py", ""))

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

def loadMod(module, argument=None):

    module = __import__(module)
    
    if module == "scan_port": 
        
        target = module.ScanMachine(argument)
        
    elif module == "scan_subnet":

        target = module.SubnetScan(argument)

def welcomeMess():
    print("""\
Author : Pixailz
git : https://github.com/Pixailz/PyMod""")

def mainLoop():

    os.system("clear")
    welcomeMess()
    loop = True

    while loop:

        entry = input("Pix@PyMod : ").strip()
        
        if entry.split(" ")[0] == "use":
          
            if len(entry.split()) > 1 and entry.split(" ")[1] in modules:
              
                mod = entry.split(" ")[1]
                arg = "|".join(entry.split(" ")[2:])
                loadMod(module=mod, argument=arg)
                
            else:
              
              printHelp(arg=1)
        
        elif entry == "cls":
  
            os.system("clear")
 
        elif entry == "exit":
          
            break

        elif entry == "help":
          
            printHelp()

        else:

            print("command not found")

def main():
    init()
    mainLoop()

main()
