#!/usr/bin/env python3
def tipp_eingabe_check(tipp):
    #Ueberprüfung der Liste 'tipp' nach gültigkeit
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

    #print("Ihr Tipp", *tipp)

def lotto_ziehung():
    #erzeugt eine Liste 6 aus 49
    import random
    ziehung = sorted(random.sample(range(1,50), 6))
    print("Die Ziehung lautet: ", ziehung)

def tipp_auswertung(tipp, ziehung):
    #vergleiche Liste 'tipp' mit liste 'ziehung'
    print("Tipp: ", tipp)
    print("Ziehung: ", ziehung)

    points = 0

    for w,n in zip(ziehung,tipp):
        if w == n:
            points += 1
    print("Du hast: ", points, "richtige Zahlen.")

