#!/usr/bin/env python3

# import the json module
import json

# Read in the contents of our file into a list
with open("devasc-topics.txt", "r") as finput:
    lines = finput.read().splitlines()

output = []

for line in lines:

    # Percentage values
    # --------------------------------------------------------------------------
    if "%" in line:
        output[-1]["percentage"] = line
        continue

    # Section headlines
    # --------------------------------------------------------------------------
    # E.g., "1.0 This title"
    # E.g., "1.3.a This other title"

    # Split into the section number and section title.
    # E.g., "1.0 This title" => number = "1.0", title = "This title"
    number, title = line.split(" ", 1)

    # Create the framework for the section object
    section = {
        "number": number,
        "title": title
    }

    # Major Sections
    # --------------------------------------------------------------------------
    if number[1] == "0":
        output.append(section)
        continue

    # Sub-sections
    # --------------------------------------------------------------------------
    # Section numbers get split up into component parts.
    # E.g., "1.3" => ["1", "3"]
    # E.g., "1.3.a" => ["1", "3", "a"]
    number = number.split(".")

    # If this is our first subsection, we need to create the sections property
    if not "sections" in output[-1].keys():
        output[-1]["sections"] = []

    output[]["sections"].append(section)

output = json.dumps(output, indent=4)
print(output)
