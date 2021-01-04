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

def truncate(t):

    return t[:t.find(".") + 3]

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

def isup(target, exitOnFail=False):

    if os.name == "posix":

        ping = subprocess.run(["ping", "-c", "1", "-s", "0", target], stdout=subprocess.PIPE)

    elif os.name == "nt":

        ping = subprocess.run(["ping", "-n", "1", "-l", "0", target], stdout=subprocess.PIPE)

    if "ttl=" in str(ping.stdout).lower():

        print(f"\n{target} is up\n")
        return True

    else:

        if exitOnFail:

            print(f"\n{target} is down, exiting ...\n")
        
        else:
            
            return False

def cs():

    if os.name == "posix":

        os.system("clear")

    elif os.name == "nt":

        os.system("cls")

if __name__ == "__main__":
    pass