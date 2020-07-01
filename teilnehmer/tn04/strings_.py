#!/usr/bin/env python3
import os
import sys

fname = "/home/coder/python_grundlagen/materialien/SampleLog.log"

with open(fname, "r") as f:
   daten = f.read()

#print(daten)
#print(len(daten))
#print(daten[0:100])
#print(daten[-100:])

target = "127.0.0.1"
#print(target in daten)
#print(daten.find(target))
#print(daten.rfind(target))



#while lfdwert <= endwert:
#    print (lfdwert)
#    lfdwert = lfdwert + 1
position = 0
last = daten.rfind(target)

while position <= last:
      position = daten.find(target, position)
      print("-->", position)
      position += 1