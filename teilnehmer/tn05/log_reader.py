#!/usr/bin/env python3
import os
import sys

fpathin = "/home/coder/python_grundlagen/materialien/" 
fpathout = "/home/coder/python_grundlagen/teilnehmer/tn05/"
fname = "/home/coder/python_grundlagen/materialien/SampleLog.log"

with open(fname, "r") as f:
    #daten = f.read()
    daten = f.readlines()  # liste mit \n

# y = daten.split("\n")   # ohne \n
# print("Zeilen " + str(len(y)))

print(type(daten))

for pos, zeile in enumerate(daten, 1):
    if "127.0.0.1" in zeile:
        print(pos, zeile.strip())



maxlen = (len(daten))
print(maxlen)


#x = daten.find("127.0.0.1")
#print("gefunden: " + str(x))
#while x <= maxlen:
#    x = daten.find("127.0.0.1", x+1)
#    print("gefunden: " + str(x))
#    if x == -1:
#        exit()





