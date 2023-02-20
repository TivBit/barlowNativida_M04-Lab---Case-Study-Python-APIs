# -*- coding: utf-8 -*-
"""
Created on %(Date: 19 Feb 2023)s

@author: %(Tiv Barlow)s
Python Version 3.11.1
SDEV 220 Spring 2023
Assignment: M04 Lab - Case Study: Python APIs
"""

class Book():
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        
    def __eq__(self, other):
        if isinstance(other, Book):
            return (self.year == other.year)
        
    def __repr__(self):
        return f"{self.title} is a book written by {self.author} and published in the year {self.year}."