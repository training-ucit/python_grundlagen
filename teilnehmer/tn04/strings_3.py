#!/usr/bin/env python3
fname = "/home/coder/python_grundlagen/materialien/SampleLog.log"

with open(fname, "r") as f:
   daten = f.readlines()

print(type(daten))

target = "127.0.0.1"
pos = 0
for zeile in daten:
    pos += 1
    if target in zeile:
        print(zeile.strip())

