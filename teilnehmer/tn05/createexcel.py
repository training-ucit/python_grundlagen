#!/usr/bin/env python3
import os
import sys
import csv
import datetime


def read_quotes(fname):
    quotesdict = {}
    with open(fname) as f:
        quotesdict = csv.DictReader(f)
    return quotesdict


def daten_aufbereitung(daten):
    None
#   neu_daten = []
         
    return neu_daten




# y = daten.split("\n")   # ohne \n
# print("Zeilen " + str(len(y)))


if __name__ == "__main__":
   fname = "/home/coder/python_grundlagen/materialien/HistoricalQuotes.csv"
   daten = read_quotes(fname)
   print(daten)
   

#x = daten.find("127.0.0.1")
#print("gefunden: " + str(x))
#while x <= maxlen:
#    x = daten.find("127.0.0.1", x+1)
#    print("gefunden: " + str(x))
#    if x == -1:
#        exit()





