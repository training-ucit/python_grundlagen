#!/usr/bin/env python3
import sys

try:
    quelle = input("Quelldatei: ")
    with open(quelle) as f:
        daten = f.read()
    print(len(daten))
    ziel = input("Zieldatei: ")
    with open(ziel, "w") as f:
        f.write(daten)
    print("Fertig!")
except:
    print ("Unexpected error:", sys.exc_info()[0])
    print("Es ist was schiefgelaufen!")
