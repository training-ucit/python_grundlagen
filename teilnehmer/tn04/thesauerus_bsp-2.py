#!/usr/bin/env python3
fname = "/home/coder/python_grundlagen/materialien/100 Sales Records.csv"

csv_daten = []

with open(fname) as f:
    # Erste Zeile (header) lesen
    headerdaten = f.readline().strip().split(",")
    # Alle weiteren Zeilen lesen
    for zeile in f:
        werte = zeile.strip().split(",")
        # Ein dictionary erstellen....
        dictionary = {}
        for pos, feld in enumerate (headerdaten):
            dictionary[feld] = werte[pos]
        # Zeile 14 - 16 in kürzerer Form: dictonary = dict(zip(headerdaten, werte))
        #... und hier wird das dictionary an die CSV Liste angehängt
        csv_daten.append(dictionary)    

try:
    print(len(csv_daten))
    print(csv_daten[0])
    print(csv_daten[0]["Region"], csv_daten[0]["Units Sold"], csv_daten[0]["Ship Date"])
except KeyError:
    print("Fehler")