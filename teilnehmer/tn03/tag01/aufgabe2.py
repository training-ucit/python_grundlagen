#!/usr/bin/env python3

"""This script prompts a user to enter a filename, reads file, get 2nd filename and writes it back"""

in_file = input("Filename to read:")

try: 
        with open(in_file, "r") as f:
            file_content = f.read()
except FileNotFoundError: 
    print(f"Error: File '{in_file}' not found")
    exit(1)
except: 
    print (f"Error: File '{in_file}' open general error")
    exit(2)


out_file = input("Filename to write:")

try: 
    print(f"writing file '{out_file}'")
    with open(out_file, "w") as f:
        f.write(file_content)
except: 
    print (f"Error: File '{out_file}' could not be written")
    exit(2)


    