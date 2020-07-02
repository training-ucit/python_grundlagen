#!/usr/bin/env python3
import game
import user
import random

tipp = user.tipp_input()

if game.tipp_eingabe_check(tipp) == True:
    ziehung = game.lotto_ziehung()
    print(f"Ergebnis: {game.tipp_auswertung(tipp, ziehung)}")
else:
    print("Fehler im Tipp")
