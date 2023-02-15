# -*- coding: utf-8 -*-
"""
Created on %(Date: 12 Feb 2023)s

@author: %(Tiv Barlow)s
Python Version 3.11.1
SDEV 220 Spring 2023
Assignment: M04 Programming Assignment - Modules and Databases
Chapter 16 Task: 16.8
"""

from flask import Flask
application = Flask(__name__)


class Book(): 
    def __init__(self, Id, book_name, author, publisher):
        self.id = Id
        self.book_name = book_name
        self.author = author
        self.publisher = publisher
        
    def __str__(self):
        return f"{self.title} was written by {self.author} in {self.year}"
    
books = [
    Book(123, "The Weirdstone of Brisingamen", "Alan Garner", "The Write Brothers"),
    Book(456, "Perdido Street Station", "China Miéville", "New Albany Publishing"),
    Book(789, "Thud!", "Terry Pratchett", "Clarksville Maniacs" ),
    Book(101,"The Spellman Files", "Lisa Lutz", "Ivy Tech Essays"),
    Book(112, "Small Gods", "Terry Pratchett", "Makin this one up")
    ]


######################## JSON

import json


with open("books2.json") as fromFile:
    data = []
    for line in fromFile:
        data.append(json.loads(line.strip()))
        
@application.route("/books")
def bookbag():
    with open("books2.json") as fromFile:
        for line in fromFile:
            yield line.strip()
            
@application.route("/books/<year>")
def bookbag_year(year):
    with open("books2.json") as fromFile:
        
            def year(Id, book_name, author, publisher):
                
            #Iterate through lines
              for i, line in enumerate(fromFile):
            
                #Choose specific ID to print.
                if Id == Id:
                    print(line)
                                    
                else:
                    return "There are no books with the ID (Id)}."
                   
            print(line)
            yield "hello world"
            
            
        