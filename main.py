#!/usr/bin/python3

import markdown2
from docx import Document
from docx.shared import Inches


#document.save("test.docx")


class Dog:
   def __init__(self, name, age):
      self.age = age
      self.name = name

   def he_is_so_old(self): # I forgot to add the 'self' and i put "theo" instead of self in the method. 
      print ("OMG " + self.name + " is already " + self.age)

theo = Dog("theo-beo", "10 months")
theo.he_is_so_old()

# Output: => "OMG theo-beo is already 10 months"

# --  -- -- -- -- -- -- -- -- -- --

# Order of the script

# Import libraries ------

   # Markdwon2, pytho-docx 

# instantiate helper methods or classes ------

# ---- create a class for recieving and processing markdown

# ---- pulling from the directory that inkdrop stores markdown

# ---- process errors at the beginning to make sure all markdown is comptabible with 'markdown2'    

# ---- create a class for cleaning and creating a new word document

      # translate the markdown into the library's (python-docx) 'add' method equivalents

      # store as dict with the markdown and the helper method (key : value) 

      # create a new document (copy) from the status-report template file 

      # use a function to loop through the dict and add the markdown content into the new document 

      # save dynamically with 'status-report' + today() and then save to desktop or icloud desktop.  

      # add to PATH of work computer and find a fast way to execute the scrip (CLI or icon or make into MacOSX application)

# ---- create main method to fully execute the all steps.   
