#!/usr/bin/env python3.6

import os
import sys

src_file = "/home/coder/python_grundlagen/materialien/SampleLog.log";
search_pattern = "127.0.0.1"
try:
    with open(src_file, "r") as src:
        text = src.read ()
        list = text.split("\n")
        print (len(list))
        for i in range (0,len(list)):
            #print (list[i])
            pos = list[i].find(search_pattern)
            while pos >= 0 :
                print(i, pos)
                print (list[i])
                pos = list[i].find(search_pattern, pos+1)
except Exception as e:
    print ("Unexpected error:", e)
    raise
finally:
    print ("Finita")



