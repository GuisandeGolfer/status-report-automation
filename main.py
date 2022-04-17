#!/usr/bin/python3
from __future__ import print_function

from datetime import date
from docx import Document
from docx.shared import Inches 
from markdown2 import Markdown
import mammoth

# Change to absolute location of status report template file [x] 

# change these file locations based on what computer I am on. 

# template = "/Users/dguisande/Library/Group Containers/UBF8T346G9.Office/User Contenf.localized/Templates.localized/\~\$-Berkeley-Meeting-Agenda.dotx"
#template = "templatecopy.docx"

#document = Document(template)

#iteration = 3
#current_run = iteration + 1

#document.save("new-template-" + str(current_run)  + ".docx") 

# = = = = = = = = = = = = = = = =

#markdowner = Markdown() 

#print(markdowner.convert("*boo!*"))

# --  -- -- -- -- -- -- -- -- -- --
with open("templatecopy.docx", "rb") as docx_file:
    result = mammoth.convert_to_html(docx_file)
    text = result.value
    with open('template-output.html', 'w') as text_file:
        text_file.write(text)

'''
    I need to 'open' the md file, and insert certain blocks of text into the method defined on line 11, 
    once that is complete, I can write to a file that is built of the 'template' defined at the beginning go the script. 


    Food for thought: Can you convert a word document into a html file?
        yes, I can, so maybe I can translate md -> html -> word-document
'''







