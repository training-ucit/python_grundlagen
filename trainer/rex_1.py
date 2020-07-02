import re
import pprint

fname = "/home/coder/python_grundlagen/materialien/SampleLog.log"
with open(fname) as f:
    zeilen = f.readlines()

pattern = r"^\d{2}/\d{2}"
rex = re.compile(pattern)
ergebnis = []
for zeile in zeilen:
    if not rex.match(zeile):
        ergebnis.append(zeile.strip())

pprint.pprint(ergebnis)
