#!/usr/bin/env python3
import os
import sys

startwert = 1
endwert = 50

for n in list(range(startwert, endwert+1)):
    if n % 2 == 0:
        print("Gerade: " + str(n))
    else:
        print("Ungerade: " + str(n))
        