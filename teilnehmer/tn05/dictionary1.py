#!/usr/bin/env python3
import os
import sys

homedir = os.environ["HOME"]
print(homedir)

tipp = []
zahl = 0
i = 1

# fname = f"{os.environ["HOME"]}/python_grundlagen/materialien/openthesaurus.txt."

thesaurus ={}

with open(fname) as f:
    if zeile in f:
        if not zeile.startwith("#") and not zeile.startwith(" ")
            wrote = zeile.strip()split(";")
            thesaurus[wrote[0]] = wrote[1:]

# pprint.pprint[thesaurus]

print(thesaurus["Änderung"])

# anstatt try catch
print(thesaurus.get("Daddel", "< nicht gefundne >"))

print(list(thesaurus.keys())[:5])


# y = daten.split("\n")   # ohne \n
# print("Zeilen " + str(len(y)))


try:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)



except ValueError:
    print("fehlerhafter wert")




