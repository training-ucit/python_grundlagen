#!/usr/bin/env python3.6

import os
import sys

src_file = "/home/coder/python_grundlagen/materialien/100 Sales Records.csv"
dicti_list = []
keys = []

try:
    with open(src_file, "r") as src:
        keys = src.readline().strip().split(',')
        for line in src :
            data = line.strip().split(',')
            dicti_entry = {}
            for col, value in enumerate(data):
                dicti_entry[keys[col]] = value
            dicti_list.append (dicti_entry)
except Exception as e:
    print ("Unexpected error:", e)
    raise
finally:
    print ("Finita")

print ("Entry 0: " + str(dicti_list[0]) + "\n")
print ("Entry 10: " + str(dicti_list[10]) + "\n")

