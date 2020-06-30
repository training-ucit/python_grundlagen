#!/usr/bin/env python3
eingabe = input("Eine Eingabe bitte: ")
print("Eingegben wurde: " + eingabe)

# Eingabe Type ausgeben:
print("Der Typ ist: " + str(type(eingabe)))

# Berechnung:
ergebnis = 4711 + int(eingabe)
print("Ergebnis ist: " + str(ergebnis))