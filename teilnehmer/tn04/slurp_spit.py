#!/usr/bin/env python3
### Datien lesen (slurp) und schreiben (spit)
def slurp(fname):
    with open(fname) as f:
        return f.read()

def spit(fname, data):
    with open(fname, "w") as f:
        f.write(data)


# Filecopy: 
fname = "/home/coder/python_grundlagen/materialien/SampleLog.log"

daten = slurp(fname)
print(type(daten))
print(len(daten))
spit("/home/coder/python_grundlagen/teilnehmer/tn04/neudaten.txt", daten)       