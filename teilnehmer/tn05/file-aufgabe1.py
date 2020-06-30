#!/usr/bin/env python3
import os
import sys

fpathin = "/home/coder/python_grundlagen/materialien/" 
fpathout = "/home/coder/python_grundlagen/teilnehmer/tn05/"

try:

    eingabe = input("Dateiname import:")
    with open(fpathin + eingabe, "r") as f:
        daten = f.read()

    print(len(daten))

    ausgabe = input("Dateiname export:")
    with open(fpathout + ausgabe, "w") as f:
        f.write(daten)
except: 
    print("ein Fehler", sys.exe_info()[0])

