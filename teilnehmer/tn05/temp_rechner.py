#!/usr/bin/env python3
import os
import sys

startwert = 1
endwert = 9
einheitin = None
einheitout = None
einheiten = list(("c", "f", "k"))

einheitin = input("Umrechnen von c, f, k :")
einheitout = input("Umrechnen in  c, f, k :")
wertin = input("Temp: ") 
tempwert = float(wertin)


try:
    
    if einheitin in einheiten and einheitout in einheiten:
        print("Umrechnung: " + einheitin + "2" + einheitout) 
        if einheitin + einheitout == "cf":
            #print(einheitin + einheitout)
            if tempwert >= -273.15:
                print(9/5 * tempwert + 32)
            else:
                print("Fehler: unmögliche Temperatur!")
        if einheitin + einheitout == "ck":
            #print(einheitin + einheitout)
            if tempwert >= -273.15:
                print(tempwert + 273.15)
            else:
                print("Fehler: unmögliche Temperatur!")

        if einheitin + einheitout == "kf":
            #print(einheitin + einheitout)
            if tempwert >= 0.0:
                print(tempwert*1.8 - 459.67)
            else:
                print("Fehler: unmögliche Temperatur!")
        if einheitin + einheitout == "kc":
            #print(einheitin + einheitout)
            if tempwert >= 0.0:
                print(tempwert - 273.15)
            else:
                print("Fehler: unmögliche Temperatur!")

        if einheitin + einheitout == "fk":
            #print(einheitin + einheitout)
            if tempwert >= -459.67:
                print((tempwert + 459.67)/1.8)
            else:
                print("Fehler: unmögliche Temperatur!")
        if einheitin + einheitout == "fc":
            #print(einheitin + einheitout)
            if tempwert >= -459.67:
                print((tempwert - 32) * 5/9)
            else:
                print("Fehler: unmögliche Temperatur!")

    else:
        print("Falsche Einheit")
        exit()    
    
except ValueError:
    print("fehlerhafter wert")

finally:
    print("immer")
