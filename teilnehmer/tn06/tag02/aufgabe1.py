#! /usr/bin/env python3

quelle = "SampleLog.log"
pattern = "127.0.0.1"
count = 0
linenumber = 0
try:
    with open(quelle) as f:
        zwischenspeicher = f.read()

    if pattern in zwischenspeicher:
        maxcount = zwischenspeicher.rfind(pattern)
        while count < maxcount:
            count = zwischenspeicher.find(pattern,count+1)
            print(f"Position: {count}")

    lines = zwischenspeicher.split("\n")
    for line in lines:
        linenumber += 1
        if pattern in line:
            print(f"Line {linenumber}: {line}")

    for zeile, line in enumerate(lines, 1):
        if pattern in line:
            print(f"Zeile {zeile}: {line}")

except e:
    print("something went wrong:\n" + e)

