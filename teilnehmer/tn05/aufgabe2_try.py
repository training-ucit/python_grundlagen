#!/usr/bin/env python3
import os
import sys

startwert = 1
endwert = 9
eingabe = input("ein wert:")


try:
    wert = int(eingabe)    
    print(wert * wert)

except ValueError:
    print("fehlerhafter wert")

finally:
    print("immer")