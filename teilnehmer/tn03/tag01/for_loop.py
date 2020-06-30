#!/usr/bin/env python3
import os
import sys

startw = 1
endw   = 9

for i in range(startw,endw+1) :
    print(i)

print("*"*30)   

for n in range(1,14):

    if n % 2 == 0: 
        print(str(n) + " - grade")
    else:
        print(str(n) + " - ungrade")    

print("*"*30) 