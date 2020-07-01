#!/usr/bin/env python3
import os
import pprint
fname = "{}/python_grundlagen/materialien/openthesaurus.txt".format(os.environ["HOME"])
thesaurus = {}
with open(fname) as f:
    for zeile in f:
        if not zeile.startswith("#") and not zeile.startswith(" "):
            worte = zeile.split(";")
            thesaurus[worte[0]] = worte[1:]
print(thesaurus)

print(*thesaurus["Änderung"])
try:
    print(*thesaurus["Daddel"])
except KeyError:
    print("Nicht bekannt")

print(thesaurus.get("Daddel", "<nicht gefunden>"))

print(list(thesaurus.keys())[:5])

