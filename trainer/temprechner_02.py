#!/usr/bin/env python3
try:
    wert = float(input("Temperatur: "))
except:
    print("Ungültiger Wert")
    exit(1)

einheit = input("Quelleinheit - C F K: ")
if einheit != "C" and einheit != "F" and einheit != "K":
    print("Ungültige Einheit")
    exit(2)

ziel = input("Zieleinheit - C F K: ")
if ziel != "C" and ziel != "F" and ziel != "K":
    print("Ungültige Einheit")
    exit(3)

if (einheit == "K" and wert < 0) or (einheit == "C" and wert < -273.15) or (einheit == "F" and wert < -459.67):
    print("Zu tiefe Temperatur")
    exit(4)

result = wert

if einheit == "C":
    if ziel == "F":
        result = 32.0 + 1.8 * wert
    elif ziel == "K":
        result = 273.15 + wert

elif einheit == "K":
    if ziel == "C":
        result = wert - 273.15
    elif ziel == "F":
        result = wert * 1.8 - 459.67

elif einheit == "F":
    if ziel == "C":
        result = 5.0 * (wert - 32.0) / 9.0
    elif ziel == "K":
        result = (fahrenheit + 459.67) / 1.8

print(wert, einheit, "=", result, ziel)