#! /usr/bin/env python3
import sys

zielwert = None

einheit = input("Bitte Ursprungseinheit angeben (C, F, K): ")
if einheit not in ["C", "F", "K"]:
    print("Es geht nur C,F oder K")
    exit()

zieleinheit = input("Bitte Zieleinheit angeben (C, F, K): ")
if zieleinheit not in ["C", "F", "K"]:
    print("Es geht nur C,F oder K")
    exit()

try:
    eingabe = float(input("Bitte eine Temperatur eingeben: "))
    if (einheit == "K") and (eingabe < 0.0):
        print("Für Kelvin sind nur positive Werte erlaubt")
        exit()
except:
    print("Fehler: War das eine Zahl?")

print(f"Rechne {eingabe} {einheit} in {zieleinheit} um:")

try:
    if einheit == zieleinheit:
        print(f"Das ist leicht :-) {eingabe} {zieleinheit}")
        exit()

    if einheit == "C":
        print("Rechne von Celsius um:")
        celsius = eingabe
    if einheit == "F":
        print("Rechne von Fahrenheit um:")
        celsius = 5/9*(eingabe-32)
    if einheit == "K":
        print("Rechne von Kelvin um:")
        celsius == eingabe-273.15

    print(f"Das sind {celsius} C")

    if zieleinheit == "C":
        print("Rechne in Celsius um")
        zielwert = celsius
    if zieleinheit == "F":
        print("Rechne in Fahrenheit um")
        zielwert = (celsius+32)*9/5
    if zieleinheit == "K":
        print("Rechne in Kelvin um:")
        zielwert = celsius + 237.15

    print(f"{eingabe} {einheit} sind {zielwert} {zieleinheit}")
except:
    print("Fehler! ")