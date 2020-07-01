#!/usr/bin/env python3

eingabe = input("Ein Wert ")

# proaktive Fehlerbehandlung
if eingabe.isnumeric():
    wert = int(eingabe)
    print(wert * wert)
else:
    print("War wohl nix")

# reaktive Fehlerbehandlung
#try:
#    wert = int(eingabe)
#    print(wert * wert)
#except ValueError as fehler:
#    print("Das mit der Eingabe war wohl nix")
#    print(fehler)
     