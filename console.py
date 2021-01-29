#coding:utf-8

import sys
import os

modules = []

availlable_command = [
    "list",
    "exit",
    "load",
    "help"
]

def init():

    try:

        for v in os.listdir("./modules"):

            modules.append(v.replace(".py", ""))

    except FileNotFoundError:
        
        print(f"modules folder not found, exiting ..")
        exit()

def loadMod(module, argument=None):
    
    
    
    print(f"module loaded : {module}\n\
arg passed : {argument}")

def printHelp():
    print("list of available command : ")
    for v in availlable_command:

        print("    ",v)

def printMod():
    
    for mod in modules:
        print(f"    {mod}")

def welcomeMess():
    print("Welcome to my terminal\n\
Author : Pixailz\n\
git : https://github.com/Pixailz/PyMod")

def mainLoop():

    os.system("clear")
    loop = True

    while loop:

        entry = input("Pix@PyMod : ").strip()
        
        if entry.split(" ")[0] == "use":
          
            if len(entry.split()) > 1 and entry.split(" ")[1] in modules:
              
                mod = entry.split(" ")[1]
                arg = "|".join(entry.split(" ")[2:])
                loadMod(module=mod, argument=arg)
                
            else:
              
              printMod()
        
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
    #welcomeMess()
    mainLoop()

main()
