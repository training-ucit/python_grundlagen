#!/usr/bin/env python3

#import shop
#import user
import game

try:
    #tipp = game.tipp_eingabe()
    #tipp = [23, 65, 23, 12, 1, 4] #falsch, weil 65 > 49
    tipp = [12, 21, 42, 16, 4, 7] #ok
    valide = game.tipp_check(tipp)
    if valide == True:
        ergebnis = game.ziehung(tipp)
        treffer = game.tipp_auswertung(tipp, ergebnis)
        print(f"Dein Tip {tipp} hat bei der Ziehung der Zahlen {ergebnis} {treffer} Richtige")
    else:
        print(f"Der Tipp {tipp} entspricht nicht den Erwartungen")
except Exception as e:
    print(e)

