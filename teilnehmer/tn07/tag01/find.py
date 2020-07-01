#!/usr/bin/env Python3
with open("/home/coder/python_grundlagen/materialien/SampleLog.log", "r") as f:
    daten = f.read()

#print(len(daten))
daten = f.read()

stelle=0
while 1 == 1:

    muster = "127.0.0.1"
    occur = daten.find(muster)