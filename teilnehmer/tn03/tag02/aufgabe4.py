#!/usr/bin/env python3


''' script to find lines with specific lines in a log file '''

TARGET = "127.0.0.1"

FNAME = "/home/coder/python_grundlagen/materialien/SampleLog.log"

with open(FNAME, "r") as f:
    text = f.read()

zeilen = text.split("\n")
zeilen_nummer = 1
for zeile in zeilen:
    if TARGET in zeile:
        print(f"{zeilen_nummer} : {zeile}")
    zeilen_nummer += 1

#pos = text.find(target)

#while pos != -1:
#    if pos != -1:
#        print(pos)
#    pos = text.find(target, pos+1)
   