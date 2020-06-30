#!/usr/bin/env python3

# Eingabe prüfen und wenn 
#eingabe = input("Eine Eingabe bitte: ")
#while eingabe != str("Stop"):
#    print(eingabe)
#    eingabe = input("Die Eingabe war: ")

# Strich ausgeben zur Trennung:
print("-"*20)

### Bessere Variante (else ist nicht erforderlich, 
### da bei Eingabe von "Stop" durch den break die Schleife verlassen wird):
while True:
    eingabe = input("Kommando: ")
    if eingabe == "Stop":
        break   
    else:
        print("Die Eingabe war: "+ eingabe)