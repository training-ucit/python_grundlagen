#!/usr/bin/env python3

Temperatur = float(input("Gib die Temperatur ein: "))
Inputeinheit = input("Gib die Einheit an: [K,C,F]: ")
Outputeinheit = input("Was solls werden: [K,C,F]: ")

if Outputeinheit == "K":
    if Inputeinheit == "C":
        if Temperatur < -273.15:
            print("Fehleingabe, unmoegliche Temperatur!")
        else:
            kelvin = Temperatur + 273.15
            print("ist in Kelvin: ", kelvin)
    if Inputeinheit == "F":
        if Temperatur < -459.67:
            print("Fehleingabe, unmoegliche Temperatur!")
        else:
            kelvin = (Temperatur + 459.67)/1.8
            print("ist in Kelvin: ", kelvin)
if Outputeinheit == "C":
    if Inputeinheit == "K":
        if Temperatur < 0.0:
            print("Fehleingabe, unmögliche Temperatur!")
        else:
            celsius = Temperatur - 273.15
            print("ist in Celsius: ", celsius)
    if Inputeinheit == "F":
        if Temperatur < -459.67:
            print("Fehleingabe, unmögliche Temperatur!")
        else:
            celsius = 5.0*(Temperatur - 32.0)/9.0
            print("ist in Celsius: ", celsius)
if Outputeinheit == "F":
    if Inputeinheit == "C":
        if Temperatur < -273.15:
            print("Fehleingabe, unmögliche Temperatur!")
        else:
            fahrenheit = 32.0 + 1.8*Temperatur
            print("ist in Fahrenheit: ", fahrenheit)
    if Inputeinheit == "K":
        if Temperatur < 0.0:
            print("Fehleingabe, unmögliche Temperatur!")
        else:
            fahrenheit = Temperatur*1.8 - 459.67
            print("ist in Fahrenheit: ", fahrenheit)