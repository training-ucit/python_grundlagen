#!/usr/bin/env python3
import os

fname = os.environ["HOME"] + "/python_grundlagen/materialien/100 Sales Records.csv"

csv_daten = []

with open(fname) as f:
    # Erst einmal den HEader lesen
    header = f.readline().strip().split(",")
    # Dann die weiteren Zeilen lesen
    for zeile in f:
        werte = zeile.strip().split(",") #  in 2.....x Zeile
        # und ein dict daraus machen ...
        d = {}
        for pos, feld in enumerate(header):
            d[feld] = werte[pos]
        # Zeile 14-16 in kürzerer Form: d = dict(zip(header, werte))
        # ... das an die Liste angehängt wird
        csv_daten.append(d)

print(len(csv_daten))
print(csv_daten[0])
print(csv_daten[0]["Region"], csv_daten[0]["Units Sold"])

print("-"*80)

for entry in csv_daten:
    print(entry["Region"], entry["Units Sold"])