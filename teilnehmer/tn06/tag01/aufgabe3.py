#! /usr/bin/env python3

zielwert = None
einheit = None
zieleinheit = None

while einheit not in ["C", "F", "K"]:
    einheit = input("Bitte Ursprungseinheit angeben (C, F, K): ")

while zieleinheit not in ["C", "F", "K"]:
    zieleinheit = input("Bitte Ursprungseinheit angeben (C, F, K): ")

try:
    eingabe = float(input("Bitte eine Temperatur eingeben: "))
    if (einheit == "K") and (eingabe < 0.0):
        print("Für Kelvin sind nur positive Werte erlaubt")
        exit()
except:
    print("Fehler: War das eine Zahl?")
    exit()

print(f"Rechne {eingabe} {einheit} in {zieleinheit} um:")

try:
    if einheit == zieleinheit:
        print(f"Das ist leicht :-) {eingabe} {zieleinheit}")
    else:
        if einheit == "C":
            print("Rechne von Celsius um:")
            celsius = eingabe
        elif einheit == "F":
            print("Rechne von Fahrenheit um:")
            celsius = 5/9*(eingabe-32)
        elif einheit == "K":
            print("Rechne von Kelvin um:")
            celsius == eingabe-273.15

        print(f"Das sind {celsius} C")

        if zieleinheit == "C":
            print("Rechne in Celsius um")
            zielwert = celsius
        elif zieleinheit == "F":
            print("Rechne in Fahrenheit um")
            zielwert = (celsius*9/5)+32
        elif zieleinheit == "K":
            print("Rechne in Kelvin um:")
            zielwert = celsius + 273.15

        print(f"{eingabe} {einheit} sind {zielwert} {zieleinheit}")
except:
    print("Fehler! ")