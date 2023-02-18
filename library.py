# -*- coding: utf-8 -*-
"""
Created on %(Date: 17 Feb 2023)s

@author: %(Tiv Barlow)s
Python Version 3.11.1
SDEV 220 Spring 2023
Assignment: M04 Programming Assignment - Modules and Databases
"""

class Book():
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        
    def __eq__(self, Person):
        if self.year == 1960:
            return f"The book, {self.title} was written by {self.author}, and was published in {self.year}."
        else:
            return f"There is no in this libray published in the year {self.year}."
