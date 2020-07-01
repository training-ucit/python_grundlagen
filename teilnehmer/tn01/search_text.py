#!/usr/bin/env python3.6

import os
import sys

src_file = "/home/coder/python_grundlagen/materialien/SampleLog.log";
search_pattern = "127.0.0.1"
try:
    with open(src_file, "r") as src:
        text = src.read ()
        pos = text.find(search_pattern)
        while pos >= 0 :
            print(pos)
            pos = text.find(search_pattern, pos+1)
except Exception as e:
    print ("Unexpected error:", e)
    raise
finally:
    print ("Finita")


