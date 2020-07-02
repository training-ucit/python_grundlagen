#!/usr/bin/env python3
import json
import yaml
import pprint

fname = "/home/coder/python_grundlagen/materialien/config.json"
daten = json.load(open(fname))
# pprint.pprint(daten["web-app"]["servlet"][0]["init-param"].keys())


yaml.dump(daten, open("daten.yaml", "w"))
