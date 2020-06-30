#!/usr/bin/env python3
import os
import sys

startwert = 1
endwert = 9

lfdwert = startwert
while lfdwert <= endwert:
    print(lfdwert)
    lfdwert = lfdwert + 1

print("-"*20)

for lfdwert in range(startwert, endwert+1):
    print(lfdwert)   