#!/usr/bin/env python3

def f1(p1):
   """
      Test of assert on parameter

      @parameters: p1 of type str -
      @returns: nothing
   """
   assert isinstance(p1, str), "Invalid Datatype. Only str allowed"
   print("Jau, alles gut")


f1("A") 
f1(4711)  


