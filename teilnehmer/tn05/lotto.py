#!/usr/bin/env python3
import os
import sys

tipp = []
zahl = 0
i = 1

try:
    while i <= 6:
        zahl = int(input(str(i) + ". Zahl: "))
        if zahl < 1 or zahl > 49:
            print("Die Zahl muss zwischen 1 und 49 sein")    
        else:
            if zahl in tipp:
                print(str(zahl) + " schon getippt")
            else:
                i = i+1
                print(zahl)
                tipp.append(zahl)
                tipp.sort()
                print("Dein Tipp: ", *tipp)  # gibt einzelnen Elemente aus und keine Liste
except ValueError:
    print("fehlerhafter wert")




#for pos, zeile in enumerate(daten, 1):
#    if "127.0.0.1" in zeile:
#        print(pos, zeile.strip())


