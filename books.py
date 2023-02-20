# -*- coding: utf-8 -*-
"""
Created on %(Date: 12 Feb 2023)s

@author: %(Tiv Barlow)s
Python Version 3.11.1
SDEV 220 Spring 2023
Assignment: M04 Programming Assignment - Modules and Databases
Chapter 16 Task: 16.8
"""
import flask as Flask
from bookClass import Book

application = Flask

    
books = [
    Book("The Weirdstone of Brisingamen", "Alan Garner", 1960),
    Book("Perdido Street Station", "China Miéville", 2000),
    Book("Thud!", "Terry Pratchett", 2005),
    Book("The Spellman Files", "Lisa Lutz", 2007),
    Book("Small Gods", "Terry Pratchett", 1992)
    ]

application = Flask

@application.route("/")
def homePage():
    page = "<!DOCTYPE html><html><head><title>Sharing Splendid Book Library</title></head><body><h1>hello</h1><p>world</p></body></html>"
    return page


@application.route("/books")
def books():
    for b in books:
        yield ({"title": b.title, "author": b.author, "year": b.year}) + "\n"



@application.route("/find/by-name/<title>")
def particular(title):
    print(title)
    for b in books:
        if b.title.lower() == title:
            yield ({"title": b.title, "author": b.author, "year": b.year}) + "\n"
            

