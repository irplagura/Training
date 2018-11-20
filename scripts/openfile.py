#!/usr/local/bin/python3
import sys
import random

if len(sys.argv) < 2:
    print("Please supply a filename.")
    exit(1)

FILENAME = sys.argv[1]
F = open(FILENAME, "r")

for LINE in F:
    ENTRY = LINE.strip().split(",")    # Make a list of comma separated value
    SIZE_ENTRY = len(ENTRY)
    print (SIZE_ENTRY)
    

F.close()
