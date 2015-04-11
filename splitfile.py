#!/usr/bin/python
from ps4a import *

# inFile: file
inFile = open(WORDLIST_FILENAME, 'r', 0)
outFile = open("newlist.txt", 'w')

# wordList: list of strings
wordList = []
count = 0
for line in inFile:
    count += 1
    if count % 4 == 0:
        word = line.strip().lower()
        outFile.write(word)
        outFile.write("\n")
