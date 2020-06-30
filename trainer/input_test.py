#!/usr/bin/env python3
eingabe = input("Eine Eingabe bitte: ")
print("Eingegeben wurde: " + eingabe)
print("Der Typ ist: " + str(type(eingabe)))
ergebnis = 4711 + int(eingabe)
print("Ergebnis ist: " + str(ergebnis))