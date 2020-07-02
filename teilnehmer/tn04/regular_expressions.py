#!/usr/bin/env python3
import re

fname = "/home/coder/python_grundlagen/materialien/SampleLog.log"
with open(fname) as f:
    zeilen = f.readlines()

# finde Uhrzeit mit regular expression
pattern = r"(\d{2}):(\d{2}):(\d{2})"
rex = re.compile(pattern)

ergebnis = []
for zeile in zeilen:
    if rex.search(zeile):
        ergebnis.append(zeile.strip())

print(ergebnis)