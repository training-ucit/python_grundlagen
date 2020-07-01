#!/usr/bin/env python3
fname='/home/coder/python_grundlagen/materialien/SampleLog.log'

with open(fname) as logfile:
    text = logfile.read()

target = "127.0.0.1"
print("Erstes Finding: ", text.find(target))
position = 0
print("position: ", position)
last = text.rfind(target)
print("last: ",last)

while position <= last:
    position = text.find(target, position)
    print("In dieser Zeile ", position, " liegt das ", target)
    position +=1
