#!/usr/bin/env python3

### Reaktive Fehlerbehandlung:

eingabe = input("Eine Eingabe bitte: ")
try:
    wert = int(eingabe)
    print(wert * wert)
except ValueError as Fehler:
    print("Die Eingabe muss eine Zahl sein")
    print(Fehler)

#### ValueError ist eine Fehlerklasse: https://docs.python.org/3/library/exceptions.html