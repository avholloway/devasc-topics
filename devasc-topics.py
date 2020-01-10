#!/usr/bin/env python3

"""
Here's what we're going to do:

1. Check the command line options to make sure they're all good
2. Check that we can open the file and that it has atleast some content in it
3. Loop over the lines in the file, parsing out the section numbers, titles, and in some cases the percentage values
4. Create a python dictionary out of the contents of the file_contents
5. Print the dictionary in the content type the output is to be displayed in (command line argument)
"""

import sys
import json
import argparse
import xml.dom.minidom

def output_json():
    """Converts our blueprint object into JSON and then prints it out"""

    try:
        # attempt to parse the json document string and make it pretty
        print(json.dumps(blueprint, indent = 4))
    except:
        print("Couldn't create JSON output from that file")
        sys.exit(4)

def output_xml():
    """Converts our blueprint object into XML and then prints it out"""

    # setup our xml document string
    xml_blueprint = '<?xml version="1.0" encoding="utf-8"?><sections>'

    # loop over all of our sections
    for number, properties in blueprint["sections"].items():
        xml_blueprint += f'<section id="{number}">'

        # if this is a major section with a percentage value...
        if "percentage" in properties.keys():
            # add that as a child element
            xml_blueprint += f'<percentage>{properties["percentage"]}</percentage>'

        # add the title as a child element of the section
        xml_blueprint += f'<title>{properties["title"]}</title></section>'

    # close off our xml document string
    xml_blueprint += "</sections>"

    try:
        # attempt to parse the xml document string and make it pretty
        print(xml.dom.minidom.parseString(xml_blueprint).toprettyxml())
    except:
        print("Couldn't create XML output from that file")
        sys.exit(4)

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="an exam blueprint plain text file")
parser.add_argument("-c", "--content", help="specify either json (default) or xml")
args = parser.parse_args()

if not args.file:
    print("Please feed me a file to digest.")
    sys.exit(1)

try:
    with open(args.file, "r") as finput:
        file_contents = finput.read().splitlines()
except FileNotFoundError:
    print("Please feed me a file I can actually digest")
    sys.exit(2)

if not file_contents:
    print("Please feed me a file to digest which has content in it")
    sys.exit(3)

# container for all of our sections
sections = {}

# loop over each line in the file's contents
for i in range(len(file_contents)):
    # store a reference to the current line
    line = file_contents[i]

    # skip lines which only hold percentage values; we'll deal with them below
    if "%" in line:
        continue

    # split the line up on the first space, effectively separating the section number from the section title
    number, title = line.split(" ", 1)

    # validate number before adding?  Nah...just shove it in there
    if not number in sections.keys():
        # validate title before adding?  Nah...just shove it in there
        sections[number] = {"title":title}

    # major section titles end in .0 and a percentage value follows on the next line of the file's contents
    if number.endswith(".0") and "%" in file_contents[i+1]:
        # validate percentage before adding?  Nah...just shove it in there
        sections[number]["percentage"] = file_contents[i+1]

# stuff all of our sections in a root element
blueprint = {"sections":sections}

# which content type are we outputting for the user?
if args.content and args.content.lower() == "xml":
    output_xml()
else:
    # we default to json since json is clearly better than xml...right? right? guys? right?
    output_json()

sys.exit(0)
