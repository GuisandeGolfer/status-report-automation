#!/usr/bin/python3

import markdown2
from docx import Document
from docx.shared import Inches 

# open markdown, convert to HTML
with open('testfile.md', 'r') as f: # open given md file with read priv.

    text = f.read()

    document = Document('Hello there.docx') 
        # This method creates a new word document from the file name given. (like "create from template" button)
    document.add_paragraph('lorem ipsum dolor sit amet.')
    ''' 
    Find a way to replace 'lorem' with text from markdown, and 
    designating where I want the text to be placed, maybe there is a

    ***replace method*** or something that takes a location and text as an input.

    or just physically find the location (line number, line column) by hand
    because the template is always going to be the same
    '''
    document.save('new-document.docx') # this method saves the current document object, and renames it according to the string given

    f.close()
# write a new html file and use 'html' as the content
# with open('testwebsite.html', 'w') as f:
    # f.write(html)

# --  -- -- -- -- -- -- -- -- -- --
'''
    I need to 'open' the md file, and insert certain blocks of text into certain
    areas inside of a word document

    Food for thought: Can you convert a word document into a html file?
        yes, I can, so maybe I can translate md -> html -> word-document
'''
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
