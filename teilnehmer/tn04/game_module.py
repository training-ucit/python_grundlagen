#!/usr/bin/env python3
def eingabe_check():
    eingabe = input("Eine Eingabe bitte: ")
    print(eingabe)
try:
    wert = int(eingabe)
    print(wert)
except ValueError as Fehler:
    print("Die Eingabe muss eine Zahl sein")
    print(Fehler)