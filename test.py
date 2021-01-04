#!/usr/bin/env python3

import port_scan as ps
import sub_discovery as sd
import utils as ut


#ps.ScanMachine(target="scanme.nmap.org")
sd.SubnetScan(target="192.168.1")