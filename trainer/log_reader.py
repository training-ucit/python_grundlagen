fname = "/home/coder/python_grundlagen/materialien/SampleLog.log"

with open(fname) as f:
    text = f.read()

target = "127.0.0.1"

position = 0 
last = text.rfind(target)

while position <= last:
    position = text.find(target, position)
    print("-->", position)
    position += 1
