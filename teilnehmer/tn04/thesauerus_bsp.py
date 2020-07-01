#!/usr/bin/env python3
fname = "/home/coder/python_grundlagen/materialien/openthesaurus.txt"

thesaurus = {}
with open(fname) as f:
    for zeile in f:
        if not zeile.startswith("#") and not zeile.startswith(" "):
            worte = zeile.strip().split(";")
            thesaurus[worte[0]] = worte[1:]

try:
    print(thesaurus["Beispiel"])
except KeyError:
    print("Wort nicht vorhanden")
