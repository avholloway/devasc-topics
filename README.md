# devasc-topics
Takes the DEVASC topics/outline in plain text and converts it to JSON or XML

I made a design decision to keep the structure kind of flat, since the heirarchy is built into the section numbers.

I much rather do something like this:

   print(section["1.8.a"])

Than this:

    print(section["1"]["8"]["a"])

Anyway, this script was a challenge put forth by Steven Davidson (sdavids5670) here:

https://learningnetwork.cisco.com/message/751267#751267
