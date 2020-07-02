fname = "/home/coder/python_grundlagen/materialien/SampleLog.log"

with open(fname) as f:
    text = f.read()

#print(len(text))
#print(text[0:100])
#print(text[-100:])
#print(text[1000:2000])

#zeilen = text.split("\n")
#print(len(zeilen))
#print(zeilen[0])
#print(zeilen[-1])
#print(zeilen[-10:])

target = "127.0.0.1"
print(target in text)
print(text.find(target))
print(text.rfind(target))