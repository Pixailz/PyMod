#!/usr/bin/env python3

import time
import nmap

host = "192.168.1.254"
port = "0-1024"

def init():
    t1 = ""
    t2 = ""
    return nmap.PortScanner()

def scan_syn():
    print("SynScan Started")
    t1 = time.time()
    scanner.scan(host, port, "-T4 -sS")
    t2 = time.time() - t1
    print(t2)

def scan_udp():
    print("UDPScan Started")
    t1 = time.time()
    scanner.scan(host, port, "-T4 -sU")
    t2 = time.time() - t1
    print(t2)

def scan_full():
    print("FullScan Started")
    t1 = time.time()
    scanner.scan(host, port, "-sS -sV -sC -A -O")
    t2 = time.time() - t1
    print(t2)

def get_version():
    version_a, version_b = scanner.nmap_version()
    version = f"{version_a}.{version_b}"
    print("Nmap", version)

def get_output():

    #print(scanner.scaninfo())
    print("isup : ", scanner[host].state())

    scan_type = scanner[host].all_protocols()
    scan_type = scan_type[0]

    print("Open Ports: ", scanner[host][scan_type].keys())
    type(scanner[host][scan_type].keys())

scanner = init()
get_version()
scan_syn()
get_output()


scanner = init()
scan_udp()
get_output()

scanner = init()
scan_full()
get_output()
