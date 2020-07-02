#!/usr/bin/env python3

'''
 Log Analyser  - read file and get rid of damaged lines
 read Logfile and gives statistics to event types
'''

import re
import pprint
import collections


FNAME = "/home/coder/python_grundlagen/materialien/SampleLog.log"

erg = []; good  = []
my_dict = {}

'''
  preparation of the report
  @parameter: read liens from file
  @peturn: prepared dict for later user
'''
def report_vorbereitung(daten):
    report_dict = {}
    for l in daten:
       wort = l[15:22].strip()
       if not wort in report_dict:
           report_dict[wort] = []
       report_dict[wort].append(l)

    return(report_dict)


def read_log(fname):
    erg = []
    with open(FNAME) as f:
       for z in f:
           erg.append(z.rstrip())
    return(erg)

def write_log(fname, daten):
    with open(fname, "w") as f:
        f.write("\n".join(daten))


def daten_bearbeitung(daten):
    rex = re.compile(r"(^$)|(^ \d{2})|(Kopieren)")
    neu_daten = []
    for dat in daten:
        if not rex.search(dat):
           if re.search(r"^\d{2}", dat):
              neu_daten.append(dat)
           else:
              neu_daten[-1] += dat    

    return(neu_daten)

def report_ausgabe(report):
    
    for k in sorted(report):
       print(f"{k}: {len(report[k])}")

if __name__ == "__main__":
    daten = read_log(FNAME)
    daten = daten_bearbeitung(daten)
    report = report_vorbereitung(daten)
    print(f"Vorkommen von Message-Types in '{FNAME}'")
    report_ausgabe(report)