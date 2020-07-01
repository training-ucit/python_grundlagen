#!/usr/bin/env python3
target = "127.0.0.1"
fname="/home/coder/python_grundlagen/materialien/SampleLog.log"

with open(fname,"r") as f:
    text = f.read()
zeilen = text.split("\n")    
zeilen_nummer = 1
for zeile in zeilen:
    if target in zeile:
        print(f"{zeilen_nummer} : {zeile}")
    zeilen_nummer += 1   