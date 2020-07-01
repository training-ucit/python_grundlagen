#!/usr/bin/env python3
l = []

eingabe1 = int(input("Bitte Tipp1 abgeben: "))
eingabe2 = int(input("Bitte Tipp2 abgeben: "))
eingabe3 = int(input("Bitte Tipp3 abgeben: "))
eingabe4 = int(input("Bitte Tipp4 abgeben: "))
eingabe5 = int(input("Bitte Tipp5 abgeben: "))
eingabe6 = int(input("Bitte Tipp6 abgeben: "))


if eingabe1 in range(1,49) and eingabe2 in range(1,49) and eingabe3 in range(1,49) and eingabe4 in range(1,49) and eingabe5 in range(1,49) and eingabe6 in range(1,49):
    zahlen = eingabe1, eingabe2, eingabe3, eingabe4, eingabe5, eingabe6
    l.append(zahlen)
    print("Ihr Tipp ist: ", l)
else:
    (print("Falsche eingabe"))    

