#!/usr/bin/env python3


''' script to et lotto zahlen from stdin '''

lotto_eingabe = []

i = 0

for i in range(1,6):
    eingabe_ok = 0
    while eingabe_ok == 0:
       print(f"{i}. Zahl:", end='') 
       zahl = input()
       if zahl.isdigit():
          #if int(zahl) > 49 or int(zahl) < 1:
          if int(zahl) not in range(1,49):
              print(f"Zahl '{zahl}' nicht gueltig")
          elif zahl not in lotto_eingabe:
              lotto_eingabe.append(zahl)
              eingabe_ok=1
          else:
              print(f"Zahl '{zahl}' schon vorhanden")
       else:
           print(f"netter Versuch '{zahl}' ist keine Zahl!'")      

lotto_eingabe.sort(key=int)


print(f"Ihr Tipp: {lotto_eingabe}")     