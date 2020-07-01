#! /usr/bin/env python3

from random import seed
from random import randint

lottozahlen = list()
ziehung = list()
ergebnis = [0,0,0,0,0,0,0]
count = 0

try:
    while count < 6:
        number = int(input(f"Bitte gib Zahl {count + 1} ein: "))
        #if number < 1 or number > 49:
        if number not in range(1,50):
            print("Die Zahl muß zwischen 1 und 49 liegen")
        elif number not in lottozahlen:
            lottozahlen.append(number)
            count += 1
        else:
            print(f"Die Zahl {number} hattest Du schon")
    print(f"Dein Tip: {lottozahlen}")

    for i in range(1,10001):
        seed(i)
        count = 0
        ziehung.clear()
        while count < 6:
            number = randint(1, 49)
            if number not in ziehung:
                ziehung.append(number)
                count += 1

        count = 0
        for treffer in lottozahlen:
            if treffer in ziehung:
                count += 1
        print(f"Ergebnis von Ziehung {i}: {ziehung} - {count} Richtige")
        ergebnis[count] += 1
    print(ergebnis)

except Exception as e:
    print("Something went wrong:")
    print(e)