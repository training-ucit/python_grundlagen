#!/usr/bin/env python3.6

import os
import sys

src_file = input("Enter source file: ")
dst_file = input("Enter target file: ")

try:
    with open(src_file, "r") as src:
        data = src.read ();
        print (str(len(data)) + " bytes read from " + src_file)
        with open(dst_file, "w") as dst:
            dst.write(data);
            print ("target file " + dst_file + " written OK")
except Exception as e:
    print ("Unexpected error:", e)
    raise
finally:
    print ("Finita")

