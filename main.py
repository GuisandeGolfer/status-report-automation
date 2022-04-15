#!/usr/bin/python3
from __future__ import print_function

from datetime import date
from docx import Document
from docx.shared import Inches 
import markdown2

# Change to absolute location of status report template file [x] 

# change these file locations based on what computer I am on. 

# template = "/Users/dguisande/Library/Group Containers/UBF8T346G9.Office/User Contenf.localized/Templates.localized/\~\$-Berkeley-Meeting-Agenda.dotx"
template = "new-document.docx"

document = Document(template)

# = = = = = = = = = = = = = = = =
''' 
    This code works fine, now i need to replace the declarative 
    text with an entry from a markdown file.
'''
table = document.add_table(rows=2, cols=2)

for row in table.rows:
    for cell in row.cells:
        cell.text = 'Andrew Fitzgerald'


# = = = = = = = = = = = = = = = =

document.save("new-farts.docx")

# --  -- -- -- -- -- -- -- -- -- --
'''
    I need to 'open' the md file, and insert certain blocks of text into the method defined on line 11, 
    once that is complete, I can write to a file that is built of the 'template' defined at the beginning go the script. 


    Food for thought: Can you convert a word document into a html file?
        yes, I can, so maybe I can translate md -> html -> word-document
'''
