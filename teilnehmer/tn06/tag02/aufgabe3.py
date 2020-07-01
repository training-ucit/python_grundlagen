#!/usr/bin/env python3

import os

datei = f"{os.environ['HOME']}/python_grundlagen/teilnehmer/tn06/tag02/100 Sales Records.csv"

daten = list()
count = 1
try:
    with open(datei) as f:
        lines = f.read().split("\n")
        ueberschrift = lines[0].strip().split(",")
        #print(len(lines))
        while count in range(1,len(lines)-1):
            #print(f"Line: {count}")
            if not lines[count] == '\n':
                line = lines[count].strip().split(",")
                #print(line)
                mydict = {}
                for pos, whatever in enumerate(ueberschrift):
                    mydict[whatever] = line[pos]
                daten.append(mydict)
            #print(mydict)
            count += 1
    print(f"wrote {len(daten)} entries")
    print(f'Region: {daten[0]["Region"]}, Verkaufte Einheiten: {daten[0]["Units Sold"]}')
except Exception as e:
    print(e)