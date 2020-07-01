#!/usr/bin/env python3
tipp = []
#tip = list()

while len(tipp) < 6:
    try:
        zahl = int(input("Zahl zw 1 und 49: "))
        if zahl >= 1 and zahl <= 49:
            if not zahl in tipp:
                tipp.append(zahl)
            else:
                print("Doppelte Zahl")
        else:
            print("Ungültige Zahl")
        
    except:
        print("Fehler in der Eingabe")

print("Ihr Tipp", *tipp)