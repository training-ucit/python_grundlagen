#!/usr/bin/env python3
import os
import sys
import csv
import datetime


fname = "/home/coder/python_grundlagen/materialien/HistoricalQuotes.csv"

quotesdict = []
with open(fname) as f:
   quotesdict = csv.DictReader(f)
   for row in quotesdict:
       print(len(row))
  
  
 