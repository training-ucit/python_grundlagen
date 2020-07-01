def f1():
    print("ohne Parameter")

def f2(a):
    print("Parameter: ", a)

def f3(a, b):
    print("Parameter: ", a, b)

#f1()
#f2(4711)
#f3("HUHU", 1234)

print("-"*80)

def f4(p1=None):
    print("Parameter", p1)

def f5(p1=None, p2="HUHU"):
    print("Parameter", p1, p2)

def f6(a,p1=None, p2="HUHU" ):
    print("Parameter", a, p1, p2)

#f4()
#f4("HEY")

#f5()
#f5(p2="Alooha")

#f6("Wert1")
#f6("Wert1", p2="Noch ein Wert")

print("-"*80)

def f7(*args):
    print("Parameter:", args)

def f8(a, *args):
    print("Parameter:", a, args)

def f9(**kwargs):
    print("Parameter", kwargs)

def f10(a, **kwargs):
    print("Parameter", a, kwargs)

def f11(a, b=99, *args, **kwargs):
    print("Parameters", a, b, args, kwargs)

#f7()
#f9()
#f7(1, 2, 3)
#f9(a=1, b=2, name="Willi")

#f11(1)
#f11(1, 2)
#f11(1, 2, 3, 4, 5)
#f11(1, 2, 3, 4, 5, p1=6, p2=7)

