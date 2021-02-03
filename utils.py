#!/usr/bin/env python3

##
# HEADER
import ctypes
import os
import time
import threading
import subprocess
 #
##

def truncate(f):
    
    if type(f) is not float:
    
        raise TypeError("Le parametre attendus doit etre flottant")
    
    flottant = str(f)
    p_e, p_f = flottant.split(".")
    
    return ".".join([p_e, p_f[:2]])

def checkRoot(exitOnFail=False):

    if os.name == "posix":

        if os.geteuid() != 0: # IF NOT ROOT

            if exitOnFail:

                print("Run as Root.")
                exit()

            else:

                return False
    
        else:

            return True
    
    elif os.name == "nt":

        if ctypes.windll.shell32.IsUserAnAdmin() != 1: # IF NOT ADMIN

            if exitOnFail:

                print("Run as Admin.")
                exit()

            else:
                
                return False

        else:

            return True

def isup(target):

    if os.name == "posix":

        ping = subprocess.run(["ping", "-c", "1", "-s", "0", target], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)

    elif os.name == "nt":

        ping = subprocess.run(["ping", "-n", "1", "-l", "0", target], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)

    if "ttl=" in str(ping.stdout).lower() or "temps=" in str(ping.stdout).lower():

        return True

    else:

        return False

def menu(content, title="MENU"):

    if type(content) is not list:

        print("args should be a list")
        exit()

    loop = True

    while loop:

        sizeMenu = len(content)

        print(title.center(40, "="), end="\n\n")

        for k, v in enumerate(content):
            print(f"{k+1} : {v}")

        answer = input(f"\n(1-{sizeMenu}) : ")[:1]

        choice = list(range(1, sizeMenu + 1))
        tmp = ""

        for number in choice:
            tmp = tmp + str(number)

        choice = tmp

        if answer in choice:
            return answer

        else:
            print(f"enter a good choice (1-{sizeMenu})")
            input()
            cs()
            continue

def cs():

    if os.name == "posix":

        os.system("clear")

    elif os.name == "nt":

        os.system("cls")
  
if __name__ == "__main__":
    pass