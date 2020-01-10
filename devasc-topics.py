#!/usr/bin/env python3

import sys
import json

if len(sys.argv) < 2:
    print("Please feed me a file to digest.")
    sys.exit(1)

filename = sys.argv[-1]

try:
    with open(filename, "r") as finput:
        file_contents = finput.read().splitlines()
except FileNotFoundError:
    print("Please feed me a valid file to digest.")
    sys.exit(2)

if len(file_contents) == 0:
    print("Please feed me a filled file to digest.")
    sys.exit(3)

sections = {}

for i in range(len(file_contents)):
    line = file_contents[i]
    if "%" in line:
        continue
    number, title = line.split(" ", 1)
    if not number in sections.keys():
        sections[number] = {"title":title}
    if number.endswith(".0"):
        sections[number]["percentage"] = file_contents[i+1]

blueprint = {"sections":sections}

print(json.dumps(blueprint, indent = 4))

sys.exit(0)
