#!/usr/bin/env python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = "192.168.1.254"
port = 22

def portScanner(port):
    if s.connect_ex((host, port)):
        print(f"{port} is closed")
    else:
        print(f"{port} is open")

portScanner(port)