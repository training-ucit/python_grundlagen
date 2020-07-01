#!/usr/bin/env python3
eingabezahl = input("Eine Zahl bitte: ")
eingabewert = input("Eingabeeinheit (C, K, F): ")
ausgabewert = input("Ausgabeeinheit (C, K, F): ") 

try:
    wert = float(eingabezahl)
    if eingabewert == "C":
        if ausgabewert == "K":
            kelvin = wert + 273.15
            print("Kelvin: ", kelvin, "Gradkelvin")
        else:
            print("Wert1 ist ungültig")

    if eingabewert == "K":        
        if ausgabewert == "C":
            celsius = wert - 273.15
            print("Celsius: ", celsius, "Grad")
        else:
            print("Wert2 ist ungültig")
    
    if eingabewert == "C":
        if ausgabewert == "F":
            fahrenheit = 32.0 + 1.8*wert
            print("Fahrenheit: ", fahrenheit, "Gradfahrenheit")
        else:
            print("Wert3 ist ungültig")


except ValueError as fehler:
    print("Die Eingabe muss eine Zahl sein")
    print(fehler)