try:
    for n in range(-5, 6):
        print(n)
except ZerorError as e: 
    print("Aua")
except ArthimeticException as e:
    print("Ey")    
    raise Exception("Aua")
finally:
    print("Das wird immer erledigt")

print("Ende")

