#!/usr/bin/env python3
import sys
import os
import openpyxl
import csv

def read_quotes(fname):
    zeilen = []
    with open(fname) as f:
        for zeile in f:
            zeilen.append(zeile.strip())
    return zeilen

#def aufbereiten(daten):

#def build_xls(daten)

#def write_quotes_to_excel(fname,daten)


if __name__ == "__main__":
    fname = "/home/coder/python_grundlagen/materialien/HistoricalQuotes.csv"
   
    zeilen = read_quotes(fname)
    print(zeilen)