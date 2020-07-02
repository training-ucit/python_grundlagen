#!/usr/bin/env python3
import json

fname = "/home/coder/python_grundlagen/materialien/config.json"
daten = json.load(open(fname))
print(daten["web-app"]["servlet"][0]["init-param"].keys())




