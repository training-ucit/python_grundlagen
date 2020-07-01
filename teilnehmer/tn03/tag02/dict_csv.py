#!/usr/bin/env python3
''' script to handle thesaurus file '''
import os
import datetime

fname = f"{os.getenv('HOME')}/python_grundlagen/materialien/100 Sales Records.csv"
csv_daten = []
with open(fname) as f:
     header = f.readline().strip().split(",")   
     for zeile in f:   
         werte = zeile.strip().split(",")
         dic = {}
         for hpos, headname in enumerate(header):
             dic[headname] = werte[hpos]
         csv_daten.append(dic)

print(csv_daten[0]["Region"])
#print(csv_daten[0]["Region"])         


