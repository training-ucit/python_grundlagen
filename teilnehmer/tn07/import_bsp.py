#!/usr/bin/env python3
import sys
import pprint

pprint.pprint(sys.path)
import my_module

my_module.hello("Ulrich")
print(dir())
print(dir(my_module))