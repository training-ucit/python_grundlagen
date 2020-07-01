#!/usr/bin/env python
print("Gib 6 unterschiedliche Zahlen 1-49 ein:")
counter=1
liste = []
while counter <=6:
    print(counter, ".Zahl bitte:")
    eingabe = input("Ihre Eingabe? ")
    print (eingabe)
    if eingabe <1 or eingabe >49:
        print("Ungueltiger Wert, vielen Dank!")
        # hier noch eine neueingabe erzwingen
    if eingabe in liste:
        print("Der Wert ist bereits in der Liste, vielen Dank!")
        # hier noch eine neueingabe erwingen
    liste.append(eingabe)
    counter = counter +1
    
print("Fertig, Du gabst ein: ", liste)