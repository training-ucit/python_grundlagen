#!/usr/bin/env python3
eingabe = input("Gib Quell Datei mit Pfadnamen an: ")
with open(eingabe) as f:
    daten = f.read()
ausgabe = input("Gib Ziel Datei mit Pfadnamen an: ")
with open(ausgabe, "w") as f:
    f.write(daten)

