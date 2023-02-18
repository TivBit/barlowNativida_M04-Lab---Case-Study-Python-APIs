# -*- coding: utf-8 -*-
"""
Created on %(Date: ___)s

@author: %(Tiv Barlow)s
Python Version 3.11.1
SDEV 220 Spring 2023
Assignment: M04 Programming Assignment - Modules and Databases
"""

from library import Book

books = [
    Book("The Weirdstone of Brisingamen", "Alan Garner", 1960),
    Book("Perdido Street Station", "China Miéville", 2000),
    Book("Thud!", "Terry Pratchett", 2005),
    Book("The Spellman Files", "Lisa Lutz", 2007),
    Book("Small Gods", "Terry Pratchett", 1992)
    ]


######################## JSON

import json

with open("books2.json", "w") as toFile:
    for b in books:
        toFile.write(json.dumps({"title": b.title, "author": b.author, "year": b.year}) + "\n")
        

with open("books2.json") as fromFile:
    for line in fromFile:
        print(json.loads(line.strip()))



"""
#########################  csv

import csv

with open("books2.csv", "w") as toFile:
    writer = csv.writer(toFile)
    for b in books:
        writer.writerow([b.title, b.author, b.year])

with open("books2.csv", "r") as fromFile:
    reader = csv.reader(fromFile)
    for row in reader:
        if len(row) != 0:
            print(row)
"""
        
    