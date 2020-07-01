#!/usr/bin/env python3.6

list = []

while len(list) < 6 :
    try:
        num = int(input("Enter number please: "))
        if num not in range (1, 49) :
            print ("Value must be between 1 and 49")
        else :    
            if num in list :
                print ("Duplicate value")
            else :
                list.append(num)
    except Exception as e:
        print ("Wrong input, repeate please")
list.sort()
print("Tip ", *list)
buf = ""
for val in list :
    buf = buf + "%5d" % (val)
print(buf)

