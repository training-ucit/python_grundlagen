#!/usr/bin/env python3
import re
import pprint

def read_log(fname):
    ergebnis = []
    with open(fname) as f:
        for zeile in f:
            ergebnis.append(zeile.rstrip())
    return ergebnis

def daten_aufbereitung(daten):
    neu_daten = []
    
    rex = re.compile(r"(^ \d{2}$)|(^$)|(Kopieren)")
    for zeile in daten:
        if not rex.search(zeile):
            if re.search(r"^\d{2}", zeile):
                neu_daten.append(zeile)
            else:
                neu_daten[-1] += zeile
            
    return neu_daten

def report_vorbereitung(daten):
    report_dict = {}

    for line in daten:
        wort = line[15:22].strip()
        if not wort in report_dict:
            report_dict[wort] = []
        report_dict[wort].append(line)

    return report_dict

def write_log(fname, daten):
    with open(fname, "w") as f:
        f.write("\n".join(daten))

if __name__ == "__main__":
    fname = "/home/coder/python_grundlagen/materialien/SampleLog.log"
    daten = read_log(fname)
    daten = daten_aufbereitung(daten)
    report = report_vorbereitung(daten)
    print(report.keys())
    write_log("neudaten.log", daten)