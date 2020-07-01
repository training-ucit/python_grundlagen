#!/usr/bin/env python3
''' script to handle thesaurus file '''
import os
import datetime
import re

fname = f"{os.getenv('HOME')}/python_grundlagen/materialien/100 Sales Records.csv"
csv_daten = []
with open(fname) as f:
     header = f.readline().strip().split(",")   
     for zeile in f:   
         werte = zeile.strip().split(",")
         dic = {}
         for hpos, headname in enumerate(header):
             check_wert = werte[hpos] 
             if re.search("\d+/\d+\d+",werte[hpos]):
                 d = werte[hpos].split("/")
                 check_wert= f"{d[1]}.{d[0]}.{d[2]}"
             dic[headname] = check_wert
         csv_daten.append(dic)

#print(csv_daten[0]["Region"])
print(csv_daten[0]["Region"], csv_daten[0]["Order Date"])         


