#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

def tipp_eingabe_check(tipp):
    rval = True
    if len(tipp) != 6:
        rval = False
    elif len(set(tipp)) != len(tipp):
        rval = False
    else:
        for z in tipp:
            if z < 1 or z > 49:
                rval = False
                break
    return rval

def lotto_ziehung():
    return random.sample(list(range(1, 50)), 6)

def tipp_auswertung(tipp, ziehung):
    return list(set(tipp).intersection(set(ziehung)))

if __name__ == "__main__":
    print(tipp_eingabe_check([1,2,3,4,5,6]))
    print(tipp_eingabe_check([1,2,3,4,5]))
    print(tipp_eingabe_check([1,2,3,4,5,5]))
    print(tipp_eingabe_check([1,2,3,4,5,50]))
    
    print(lotto_ziehung())
    print(lotto_ziehung())
    print(lotto_ziehung())
    print(lotto_ziehung())

    print(tipp_auswertung([1,2,3,4,5,6], [1,2,3,4,5,6]))
    print(tipp_auswertung([1,2,3,4,5,6], [7,8,9,10,11,12]))
    print(tipp_auswertung([1,2,3,4,5,6], [5,6,7,8,9,10]))