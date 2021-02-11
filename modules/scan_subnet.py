#!/usr/bin/env python3

##
# HEADER

import sys
sys.path.append("..")

from utils import *

#
##

class SubnetScan():

    def __init__(self, target, timeout=2.5, o=True):

        self.target = target
        self.ipup = []
        self.timeout = timeout
        self.threads = []

        self.t1 = ""
        self.t2 = ""

        checkRoot(exitOnFail=True)

        self.t1 = time.time()
        self.threading()
        self.t2 = truncate(time.time() - self.t1)

        if o:
            self.output()

    def isup(self, target, x):

        if os.name == "posix":

            ping = subprocess.run(["ping", "-c", "1", "-s", "0", target], stdout=subprocess.PIPE)

        elif os.name == "nt":

            ping = subprocess.run(["ping", "-n", "1", "-l", "0", target], stdout=subprocess.PIPE)

        if "ttl=" in str(ping.stdout).lower():

            self.ipup.append(x)

    def threading(self):

        count = 0

        for x in range(0,255+1):

            ip = f"{self.target}.{x}"
            count += 1
            t = threading.Thread(target=self.isup, args=(ip,x))
            t.start()
            self.threads.append(t)

        for process in self.threads:

            process.join()

    def output(self):

        print("{} hosts scanned in {} sec\n".format(len(self.ipup), self.t2))

        self.ipup.sort(reverse=True)
        for x in range(len(self.ipup)):

            print("{}.{} is up".format(self.target, self.ipup[x]))

if __name__ == "__main__":
    SubnetScan("192.168.1")
