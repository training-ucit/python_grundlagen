#!/usr/bin/env python3
import csv

class Klasse:
    def __init__(self, wert1, wert2):
        self._w1 = wert1
        self._w2 = wert2

    def add(self):
        return self._w1 + self._w2

    def sub(self):
        return self._w1 - self._w2

class KlasseX(Klasse):
    def __init__(self, wert1, wert2):
        super().__init__(wert1, wert2)

    def mul(self):
        return self._w1 * self._w2
        
if __name__ == "__main__":
    print(dir(csv.DictReader))


#    o = Klasse(5, 7)
#    print(o)
#    print(dir(o))

    #print(o.add())
    #print(o.sub())
    #print(o.mul())

    #o_list = []

    #for v in range(1, 10):
    #    o_list.append(Klasse(v, 10))

    #print(o_list)