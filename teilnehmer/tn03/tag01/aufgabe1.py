#!/usr/bin/env python3

while True:
     eingabe = input ("Bitte ne Zahl (oder stop für ENDE): ")
     if eingabe == "stop":
         break
     else:
#         print("Eingabe: " + eingabe) 
         if eingabe.isdigit():
             print("4711 + " + eingabe + " = " + str(4711+int(eingabe)))
         else:
             print("'"+ eingabe + "'" + " ist nicht wirklich ne Zahl")    



