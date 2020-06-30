#!/usr/bin/env python3

try:
    eingabedatei = input("Dateiname zum lesen eingeben (muss im aktuellen Verzeichnis sein): ")
    with open(eingabedatei, "r") as f:
        daten = f.read()

    ausgabedatei = input("Dateiname zum schreiben eingeben(wird in aktuellens Verzeichnis geschrieben): ")
    with open(ausgabedatei, "w") as f:
        f.write(daten)
    print("Abgeschlossen")

except:
    print("Fehler")