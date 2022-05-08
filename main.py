#!/usr/bin/python3
# Import Libraries
# --  -- -- -- -- -- -- -- -- -- --
from __future__ import print_function
import mammoth
from bs4 import BeautifulSoup as bs
import re 
import os
# --  -- -- -- -- -- -- -- -- -- --

file_input = "templatecopy.docx"

def change_html_to_wordocx(file):

    with open(file, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file) 
        soup = bs(result, features="lxml")
        # use soup.find on old text
        # old_text = soup.find("widget name", {id: "id of what you want to edit"})
        # then use soup.find on new text with "re.compile" (regex) and then "replace_with()"
        # new_text = old_text.find(text=re.compile('text you want to edit')).replace_with('new text you want to replace with') 
        '''
            try to put specific id's on word-docx templates and then create regex for text and loop through two arrays, 
            1 with new text, 1 with old text, then replace
            look at pythonic post on Firebase for faster-ways to iterate over the two arrays/list/dicts/whatever
        '''
        with open('template-output.html', 'w') as text_file:
            text_file.write(prettyHTML)
            text_file.close()

change_html_to_wordocx(file_input)

'''
    I need to 'open' the md file, and insert certain blocks of text into the method defined on line 11, 
    once that is complete, I can write to a file that is built of the 'template' defined at the beginning go the script. 


    Food for thought: Can you convert a word document into a html file?
        yes, I can, so maybe I can translate md -> html -> word-document
'''
