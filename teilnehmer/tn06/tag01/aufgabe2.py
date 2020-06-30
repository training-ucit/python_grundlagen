#! /usr/bin/env python3
try:
    quelle = input("Please enter Sourcefile: ")
    ziel = input("Please enter Destinationfile: ")
    with open(quelle) as f:
        zwischenspeicher = f.read()
    with open(ziel,'w') as f:
        f.write(zwischenspeicher)
except:
    print("Something went wrong here")
finally:
    print("This is the end!")