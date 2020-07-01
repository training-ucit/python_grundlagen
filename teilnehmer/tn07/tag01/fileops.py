#!/usr/bin/env python3

def slurp(fname):
    with open(fname) as f:
        return f.read()

def spit(fname, data):
    with open(fname, "w") as f:
        f.write(data)


fname = "/home/coder/python_grundlagen/materialien/SampleLog.log" 

daten = slurp(fname)
print(type(daten))
print(len(daten))
#spit("/home/coder/neudaten.txt", daten)      