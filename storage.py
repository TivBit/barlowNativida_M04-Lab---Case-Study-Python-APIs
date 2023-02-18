# -*- coding: utf-8 -*-
"""
Created on %(Date: 12 Feb 2023)s
@author: %(Tiv Barlow)s
Python Version 3.11.1
SDEV 220 Spring 2023
Assignment: M04 Programming Assignment - Modules and Databases-Ch 16
Chapter 16 Task: 16.8
"""

class Book(): 
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        
    def __eq__(self, year):
        if year == 1960:
            return f"{self.title} written by {self.author}, Published {self.year}."
        
books = [
    Book("The Weirdstone of Brisingamen", "Alan Garner", 1960),
    Book("Perdido Street Station", "China Miéville", 2000),
    Book("Thud!", "Terry Pratchett", 2005),
    Book("The Spellman Files", "Lisa Lutz", 2007),
    Book("Small Gods", "Terry Pratchett", 1992)
    ]
"""
book_info = Book(title, author, year)
print(book_info)
"""

############## binary file

import pickle

with open("books.db.", "wb") as toFile:
    pickle.dump(books, toFile)
    

with open("books.db", "rb") as fromFile:
    book_stuff = pickle.load(fromFile)
    print(book_stuff[3])
    

############## SQLite
import sqlite3 as sql

db = sql.connect("books.db")

createQuery = "CREATE TABLE IF NOT EXISTS People(Title TEXT, Author TEXT, Year INTEGER);"

db.execute(createQuery)

for b in books:
    insertQuery = "INSERT INTO Books(Title, Author, Year) VALUES(\"" + b.title + "\", " + b.author + ", \"" + int(b.year) + "\");"
    cursor = db.execute(insertQuery)
    if cursor.rowcount >= 0:
        print("added the data")
    else:
        print("there was an error")
        
        
selectQuery = "SELECT title, author, year FROM Books ORDER BY last_name ASC;"


cursor = db.execute(selectQuery)
for row in cursor:
    print(row[0])
    
db.close()