#!/usr/bin/env python3

def menu():
    while True:
        print("(1) Umrechnung von Celsius nach Kelvin")
        print("(2) Umrechnung von Celsius nach Fahrenheit")
        print("(3) Umrechnung von Kelvin nach Celsius")
        print("(4) Umrechnung von Kelvin nach Fahrenheit")
        print("(5) Umrechnung von Fahrenheit nach Celsius")
        print("(6) Umrechnung von Fahrenheit nach Kelvin")
        print("(X) Abbruch")

        eingabe = input("Bitte wählen: ")
        valid = ["1", "2", "3", "4", "5", "6", "X"]
        einheit = ["C", "C", "K", "K", "F", "F", None]
        if eingabe in valid:
            return eingabe, einheit[valid.index(eingabe)]

def is_valid_value(wert, einheit):
    return (einheit == "C" and wert >= -273.15) or (einheit == "K" and wert >= 0) or (einheit == "F" and wert >= -473)

def get_value():
    return float(input("Temperaturwert: "))

def berechnung(wahl, wert):
    if wahl == "1":
        ergebnis = wert + 273.15
    elif wahl == "2":
        ergebnis = 32.0 + 1.8*wert
    elif wahl == "3":
        ergebnis = wert - 273.15
    elif wahl == "4":
        ergebnis = wert*1.8 - 459.67
    elif wahl == "5":
        ergebnis = 5.0*(wert - 32.0)/9.0
    elif wahl == "6":
        ergebnis = (wert + 459.67)/1.8
    return ergebnis

def main():
    wahl, einheit = menu()
    if wahl != "X":
        wert = get_value()
        if is_valid_value(wert, einheit):
            ergebnis = berechnung(wahl, wert)
            print("Ergebnis ", ergebnis)
        else:
            print("Ungültig", einheit, wert)

if __name__ == "__main__":
    main()