#!/usr/bin/python3
from __future__ import print_function
# from mailmerge import MailMerge
'''
    find an alternative to mail-merge; not working on machine or repl.it
    going to try to just use 'docx' and doing it by hand.
'''
from datetime import date
from docx import Document
from docx.shared import Inches 
import markdown2

# Change to absolute location of status report template file [x] 
template = "/Users/dguisande/Library/Group Containers/UBF8T346G9.Office/User Contenf.localized/Templates.localized/\~\$-Berkeley-Meeting-Agenda.dotx"

document = MailMerge(template)
print(document.get_merge_fields()) # This print method will show if there are any merge fields with the Berkeley template I have

'''
    in order for the code above to work, I need to assign merge fields to the template I am going to be using and once that is defined 
    this package 'mailmerge' will be able to use those as the fields to have text inserted, 
     
     and that text can be populated into a dictionary like this:

     document.merge (
        status='Gold',
        city='Springfield',
        phone_number='800-555-5555',
        etc...)

    document.write('name of new file.docx')
'''

# --  -- -- -- -- -- -- -- -- -- --
'''
    I need to 'open' the md file, and insert certain blocks of text into the method defined on line 11, 
    once that is complete, I can write to a file that is built of the 'template' defined at the beginning go the script. 


    Food for thought: Can you convert a word document into a html file?
        yes, I can, so maybe I can translate md -> html -> word-document
'''
