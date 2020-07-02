#!/usr/bin/env python3

import re
import pprint

def readlog(fname):
    lines = []
    with open(fname) as f:
        for zeile in f:
            lines.append(zeile.rstrip())
    return(lines)

def writelog(fname, daten):
    with open(fname, "w") as f:
        f.write("\n".join(daten))

def datenaufbereitung(daten):
    filtereddata = []
    rex = re.compile(r"(^ \d{2})|(^$)|(Kopieren)")
    for zeile in daten:
        if not rex.search(zeile):
            if re.search(r"^\d{2}", zeile):
                filtereddata.append(zeile)
            else:
                filtereddata[-1] += zeile
    return filtereddata

def preparereport(daten):
    report = {}
    for line in daten:
        typ = line.split(" ")[2][0:7]
        print(typ)
        if not typ in report:
            report[typ] = []
        report[typ].append(line) 
    return report

if __name__ == "__main__":
    
    dateiname = "../tag02/SampleLog.log"
    daten = readlog(dateiname)
    neuedaten = datenaufbereitung(daten)
    writelog("logfile.log", neuedaten)
    pprint.pprint(preparereport(neuedaten))