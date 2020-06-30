#! /usr/bin/env python3
eingabe = input("Eine Eingabe: ")
print("Der Wert war: " + eingabe)
print("Eingabe war vom Typ: " + str(type(eingabe)))
ergebnis = 42 + int(eingabe)
print("Ergebnis ist " + str(ergebnis))