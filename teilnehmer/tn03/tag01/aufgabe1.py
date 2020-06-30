#!/usr/bin/env python3

"""This script prompts a user to enter a number and print that out until stop is given"""

while True:
    eingabe = input("Bitte ne Zahl (oder stop für ENDE): ")
    if eingabe == "stop":
        break
    if eingabe.isdigit():
        print(f"4711 + {eingabe} = {str(4711+int(eingabe))}")
    else:
        print(f"'{eingabe}' ist nicht wirklich ne Zahl")
