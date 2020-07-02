#! /usr/bin/env python3

from random import seed
from random import randint

def tipp_eingabe():
    count=0
    lottozahlen = list()
    try:
        while count < 6:
            number = int(input(f"Bitte gib Zahl {count + 1} ein: "))
            #if number < 1 or number > 49:
            if number not in range(1,50):
                print("Die Zahl muß zwischen 1 und 49 liegen")
            elif number not in lottozahlen:
                lottozahlen.append(number)
                count += 1
            else:
                print(f"Die Zahl {number} hattest Du schon")
        print(f"Dein Tip: {lottozahlen}")
    except Exception as e:
        print("In tipp_eingabe")
        print(e)
    return(lottozahlen)

def tipp_check(lottozahlen):
    zwischenliste = list()
    try:
        count=0
        ok=True
        if len(lottozahlen) != 6:
            ok=False
        while count < 6:
            if lottozahlen[count] not in range(1,50):
                ok=False
            if lottozahlen[count] in zwischenliste:
                ok=False
            else:
                zwischenliste.append(lottozahlen[count])
            count += 1
    except Exception as e:
        print("in tipp_check")
        print(e)
    return(ok)

def ziehung(lottozahlen):
    ziehung = list()
    try:
        count = 0
        while count < 6:
            number = randint(1, 49)
            if number not in ziehung:
                ziehung.append(number)
                count += 1
    except Exception as e:
        print("in ziehung:")
        print(e)
    return(ziehung)

def tipp_auswertung(lottozahlen, ziehung):
    try:
        count = 0
        for treffer in lottozahlen:
            if treffer in ziehung:
                count += 1
        #print(f"Ergebnis von Ziehung: {ziehung} - {count} Richtige")
    except Exception as e:
        print("In tipp_auswertung")
        print(e)
    return(count)
        
if __name__ == "__main__":
    tipp = tipp_eingabe()
    valide = tipp_check(tipp)
    if valide == True:
        ergebnis = ziehung(tipp)
        treffer = tipp_auswertung(tipp, ergebnis)
        print(f"Dein Tip {tipp} hat bei der Ziehung der Zahlen {ergebnis} {treffer} Richtige")
    else:
        print(f"Der Tipp {tipp} entspricht nicht den Erwartungen")