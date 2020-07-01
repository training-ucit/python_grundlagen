#!/usr/bin/env python3
import os
import sys

homedir = os.environ["HOME"]
print(homedir)

csv_daten = []

fname = "/home/coder/python_grundlagen/materialien/100 Sales Records.csv"

with open(fname) as f:
    header = f.readline().strip().split(",")  # eine Zeile lesen .strip entfernt \n
#   dann die weiteren zeilen lesen
    for zeile in f:
        werte = zeile.strip().split(",") # zwei listen header und werte
        d = {}
        for pos, feld in enumerate(header):
            d[feld] = werte[pos]
        # Zeile 14-16 zwei listen in ein dict. zusammenführen dict(zip(header, werte))
        csv_daten.append(d)

print(len(csv_daten))
print(csv_daten[0])
print(csv_daten[9])
print(csv_daten[1]["Region"], csv_daten[1]["Units Sold"])

for entry in csv_daten:
    print(entry["Region"], entry["Units Sold"])
    

#    if zeile in f:
#        if not zeile.startwith("#") and not zeile.startwith(" ")
#            wrote = zeile.strip()split(";")
#            thesaurus[wrote[0]] = wrote[1:]





