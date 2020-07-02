#!/usr/bin/env python3
import os
import sys
import re
import pprint

fpathin = "/home/coder/python_grundlagen/materialien/" 
fpathout = "/home/coder/python_grundlagen/teilnehmer/tn05/"
fname = "/home/coder/python_grundlagen/materialien/SampleLog.log"

with open(fname) as f:
    zeilen = f.readlines()
    print(len(zeilen))

pattern = r""
rex = re.compile(pattern)
ergebnis = []

for zeile in zeile:
    if not rex.match(zeile):
        ergebnis.append(zeile.strip())

pprint.pprint(ergebnis)
