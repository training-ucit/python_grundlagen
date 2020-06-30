with open("/home/coder/neudaten.txt", "r") as f:
    daten = f.read()

print(len(daten))

with open("/home/coder/datenneu.txt", "w") as f:
    f.write(daten)