#!/usr/bin/env python3

'''
 RegEx Test - read file and get rid of damaged lines
'''

import re
import pprint


FNAME = "/home/coder/python_grundlagen/materialien/SampleLog.log"

erg = []; good  = []
my_dict = {}

report dict

mtypes = ["INFO", "WARN", "ERR", "TRACE"]



def read_log(fname):
    erg = []
    with open(FNAME) as f:
       for z in f:
           erg.append(z.rstrip())
    return(erg)

def write_log(filename, daten):
    with open(filename, "w") as f:
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


if __name__ == "__main__":
    daten = read_log(FNAME)
    daten = daten_bearbeitung(daten)
    write_log("neudaten.log", daten)