#!/usr/bin/env python3

##
# HEADER

import socket
import nmap3
import sys
sys.path.append("..")

from utils import *

#
##

class ScanMachine():

    def __init__(self, target, output="Screen"):

        self.output = output
        self.target = target
        self.host = ""
        self.hostname = ""
        self.ports = []

        self.t1 = ""
        self.t2 = ""

        checkRoot(exitOnFail=False)
        
        if isup(self.target):

            print(f"{self.target} is up")

        else:

            print(f"{self.target} is down, exiting ..")
            exit()

        self.validTarget()

        self.t1 = time.time()

        self.scanPort()
        
        self.t2 = truncate(time.time() - self.t1)

        self.outPut()
            
    
    def outPut(self):
        
        if self.output == "Screen":

            print("PORT\t\tSTATE\t\tSERVICE\t\tVERSION\n")

            for x in range(len(self.ports)):
                if len(self.ports[x]) == 5:
                    print(f'{self.ports[x]["portid"]}/{self.ports[x]["protocol"]}  \t{self.ports[x]["state"]}    \t{self.ports[x]["service"]}     \t{self.ports[x]["version"]}')
                
                else:
                    print(f'{self.ports[x]["portid"]}/{self.ports[x]["protocol"]}  \t{self.ports[x]["state"]}    \t{self.ports[x]["service"]}')
            
            print(f'\nHost ({self.target}) scanned in {self.t2} sec')
        
        elif self.output == "None":

            pass
        
        elif self.output == "Checker":

            report = dict()
            
            report["ip"] = self.host
            report["hostname"] = self.hostname
            report["ports"] = self.ports

            writeContent(content=report, file="test")
            
        elif self.output == "File":
            
            with open("tmp", "w") as f:
            
                print(f'''\
"ip" : "{self.host}"
"hostname" : "{self.hostname}"
"ports" : [\
''', file=f)

            count = 0

            with open("tmp", "a") as f:

                for x in range(len(self.ports)):
                    
                    count += 1
                    
                    if len(self.ports[x]) == 5:
                        
                        if count < len(self.ports):
                        
                            print(f'''\
    {{
        "portid" : "{self.ports[x]["portid"]}",
        "protocol" : "{self.ports[x]["protocol"]}", 
        "state" : "{self.ports[x]["state"]}",
        "service" : "{self.ports[x]["service"]}",
        "version" : "{self.ports[x]["version"]}"
    }},\
''', file=f)
                        else:
                            print(f'''\
    {{
        "portid" : "{self.ports[x]["portid"]}",
        "protocol" : "{self.ports[x]["protocol"]}", 
        "state" : "{self.ports[x]["state"]}",
        "service" : "{self.ports[x]["service"]}",
        "version" : "{self.ports[x]["version"]}"
    }}\
''', file=f)
                
                    else:
                    
                        if count < len(self.ports):
                    
                            print(f'''\
    {{
        "portid" : "{self.ports[x]["portid"]}",
        "protocol" : "{self.ports[x]["protocol"]}", 
        "state" : "{self.ports[x]["state"]}",
        "service" : "{self.ports[x]["service"]}"
    }},\
''', file=f)
                        else:

                            print(f'''\
    {{
        "portid" : "{self.ports[x]["portid"]}",
        "protocol" : "{self.ports[x]["protocol"]}", 
        "state" : "{self.ports[x]["state"]}",
        "service" : "{self.ports[x]["service"]}"
    }}\
''', file=f)

                print("]", file=f)

    def validTarget(self):

        try:

            socket.inet_aton(self.target)
            self.host = self.target
            hostname = socket.gethostbyaddr(self.target)
            self.hostname = hostname[0]

        except socket.error:

            self.hostname = self.target
            try:

                self.host = socket.gethostbyname(self.target)

            except socket.gaierror:

                print(f"Cannot get ip from {self.target}, exiting.")
                exit()

    def scanPort(self):

        port_s = nmap3.Nmap()
        port_o = port_s.nmap_version_detection(self.host)

        for x in range(len(port_o[self.host]["ports"])):
            OPEN_PORT = {
                "protocol" : "",
                "portid" : "",
                "state" : "",
                "service" : ""
            }

            OPEN_PORT["protocol"] = port_o[self.host]["ports"][x]["protocol"]
            OPEN_PORT["portid"] = port_o[self.host]["ports"][x]["portid"]
            OPEN_PORT["state"] = port_o[self.host]["ports"][x]["state"]
            OPEN_PORT["service"] = port_o[self.host]["ports"][x]["service"]["name"]

            if "product" in port_o[self.host]["ports"][x]["service"]:
                
                OPEN_PORT["version"] = port_o[self.host]["ports"][x]["service"]["product"]

                if "version" in port_o[self.host]["ports"][x]["service"]:

                    OPEN_PORT["version"] = OPEN_PORT["version"] + port_o[self.host]["ports"][x]["service"]["version"]

            self.ports.append(OPEN_PORT)

    def afficher(self):

        print(f"target :\t{self.target}")
        print(f"host :\t\t{self.host}")
        print(f"hostname :\t{self.hostname}")
        print(f"ports :\t\t{self.ports}")
        print(f"T1 :\t\t{self.t1}")
        print(f"T2 :\t\t{self.t2}")

if __name__ == "__main__":
    ScanMachine("scanme.nmap.org", output="Checker")