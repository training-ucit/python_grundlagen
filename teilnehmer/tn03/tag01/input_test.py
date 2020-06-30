#!/usr/bin/env python3

inp = input("give me someting: ")
print (f"Given was: ", inp)
print ("Der Typ ist: " + str(type(inp)))
erg = int(inp) + 4711
print ("4711+" + inp + "=" + str(erg))