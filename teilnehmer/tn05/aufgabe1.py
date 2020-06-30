#!/usr/bin/env python3
import os
import sys

startwert = 1
endwert = 50
run = True
eingabe = None


# for n in list(range(startwert, endwert+1)):
#    if n % 2 == 0:
#        print("Gerade: " + str(n))
#    else:
#        print("Ungerade: " + str(n))

# Varianten 
eingabe = None
while eingabe != "Stop":
    eingabe = input("Eingabe1: ")
    print(eingabe)

while 1 == 1 : # oder True oder nur 1
    eingabe = input("Eingabe2: ")
    
    if eingabe == "stop":
       break
    else:
       print(eingabe)


while True : 
    eingabe = input("Eingabe3: ")
    if eingabe == "stop":
        break
    else:
        print("Eingabe war :" + str(eingabe))

#for