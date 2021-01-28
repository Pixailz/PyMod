#coding:utf-8

import sys
import os

modules = []

def init():

    try:

        for v in os.listdir("./modules"):

            modules.append(v.replace(".py", ""))

    except FileNotFoundError:
        
        print(f"modules folder not found, exiting ..")
        exit()

def loadMod(*command):
    
    for k, v in enumerate(command):
        print(k,v)
    
    """print(f"module loaded : {module}\n\
arg passed : {arg}")"""



def welcomeMess():
    print("Welcome to my terminal\n\
Author : Pixailz\n\
git : https://github.com/Pixailz/PyMod")

def mainLoop():

    os.system("cls")
    loop = True

    while loop:

        entry = input("Pix@PyMod~: ")

        if entry.split(" ")[0] in modules:
            entry = entry.split(" ")
            loadMod(entry)

        elif entry == "exit":
            exit()

        elif entry == "help":
            print("list of available modules :")

            for v in modules:

                print("\t",v)

        else:

            print("command not found")

def main():
    init()
    #welcomeMess()
    mainLoop()

main()

