#!/usr/bin/env python3

while True: 
    eingabe = input("Kommando")
    if eingabe == "Stop":
        break
    print("Eingabe ist: " + eingabe)

# Varianten:
eingabe = None
while eingabe != "Stop":
    eingabe = input("Kommando")
    print(eingabe)

# von Victor:
while 1 == 1 : # True -> 1 == 1 -> 1
  command = input("Enter something please: ")
  print ("Entered '" + command + "'")
  if command == 'stop' :
      break

# Ab python 3.9 - ultrakurz dank Walross-Operator :=
# while (eingabe := input("Kommando")) != "Stop":
#    print(eingabe)