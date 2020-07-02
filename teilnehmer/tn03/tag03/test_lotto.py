#!/usr/bin/env python3
import lotto25


def lotto_zahlen_eingabe():

    lotto_eingabe = []

    i = 0

    for i in range(1,7):
        eingabe_ok = 0
        while eingabe_ok == 0:
            print(f"{i}. Zahl:", end='') 
            zahl = input()
            if zahl.isdigit():
                    lotto_eingabe.append(zahl)
                    eingabe_ok=1
            else:
                print(f"netter Versuch '{zahl}' ist keine Zahl!'")      

    lotto_eingabe.sort(key=int)
    return(lotto_eingabe)


lzuser = lotto_zahlen_eingabe()
lotto25.tipp_eingabe_check(lzuser)
lz = lotto25.lotto_ziehung()
print(f"{lotto25.tipp_auswertung(lzuser, lz)} Uebereinstimmungen")

