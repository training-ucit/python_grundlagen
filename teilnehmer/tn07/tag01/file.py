
!#/usr/bin/env    Python3
import os
import sys

try:

    with open("/home/coder/python_grundlagen/teilnehmer/tn07/adressen.csv", "r") as f:

    daten = f.read()

print(len(daten))

except:
    print ("Unexpected Error:", sys.exc_info

with open("/home/coder/python_grundlagen/teilnehmer/tn07/adressen.csv.new", "w") as f:
    f.write(daten)

exception(msg, *args, **kwargs)