#!/usr/bin/env python3
import os
import sys


def tipp_eingabe_check():
    try:
        i = 1
        tipp = []
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
    return tipp

def lottoziehung():
    return random.sample(list(range(1, 50)), 6)






def hellotest(name):
  print("Hello, " + name) 