#!/usr/bin/env python3
import xmltodict
import yaml
import pprint

fname = "/home/coder/python_grundlagen/materialien/books.xml"

with open(fname) as f:
    text = f.read()

xml = xmltodict.parse(text)

pprint.pprint(xml)

yaml.dump(xml, open("book.yaml", "w"))