#!/usr/bin/env python3
fname = "/home/coder/python_grundlagen/materialien/SampleLog.log"

with open(fname) as f:
    text = f.readlines()

print(type(text))

for pos, zeile in enumerate(text, 1):
    if "127.0.0.1" in zeile:
        print(pos, zeile.strip())

