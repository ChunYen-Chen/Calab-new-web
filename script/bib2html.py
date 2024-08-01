#!/bin/python3
"""
A simple tool of converting .bib to the html content of website.

How to use:
  python3 bib2html.py -h

Quick start:
  python3 bib2html.py [*.bib files]

Probably need to be modified by your usage:
  1. the authors will be highlighted => `self.highlight`
  2. html format                     => `self.add_list_element()`
  3. only the "@article" is included => `published` in `text2bibtex()`
"""

import argparse



#====================================================================================================
# Classes
#====================================================================================================
class bibtex():
    def __init__( self, bib_dict ):
        self.highlight_author = [ "Hsi-Yu Schive" ]     # The authors will be highlighted by <strong> in HTML
        self.title  = bib_dict.pop("title")
        self.author = self.clean_author( bib_dict.pop("author") )
        self.year   = bib_dict.pop("year")
        self.doi    = bib_dict.pop("doi", None)
        self.other  = bib_dict
        return

    def generate_html(self):
        # 1. title
        # 2. author
        # 3. link
        out_text = self.add_list_element( "" )
        print(out_text)
        return out_text

    def add_list_element(self, text):
        text += '<li class="text-muted publication" data-tags="%s">\n'%self.year
        text = self.add_title( text )
        text = self.add_author( text )
        if self.doi != None: text = self.add_link( text )
        text += '</li>'
        return text

    def add_title(self, text):
        text += '    <div class="publication-title">\n'
        text += '        %s\n'%self.title
        text += '    </div>\n'
        return text

    def add_author(self, text):
        text += '    <div class="publication-author">\n'
        text += '        %s\n'%self.author
        text += '    </div>\n'
        return text

    def add_link(self, text):
        text += '    <div class="publication-link">\n'
        text += '        <a href="https://doi.org/%s">doi: %s</a>\n'%(self.doi, self.doi)
        text += '    </div>\n'
        return text

    def clean_author(self, ugly_author):
        temp_author = ugly_author.split(" and ")
        out_author = []
        for author in temp_author:
            if "{" in author:
                temp1 = author.split("},")
                temp2 = temp1[1] + " "+ temp1[0][1:]
            else:
                temp2 = author

            if temp2[0] == " ":
                temp2 = temp2[1:]

            if temp2 in self.highlight_author:
                temp2 = "<strong>" + temp2 + "</strong>"
            out_author.append(temp2)
        out_author[-1] = "and " + out_author[-1]
        return ", ".join(out_author)



#====================================================================================================
# Functions
#====================================================================================================
def text2bibtex( file_name ):
    with open( file_name, "r" ) as f:
        text = ''.join( f.readlines() )

    published = True
    first_comma = True
    section = -1
    store_key = True
    store_to_dict = False
    key_name = ""
    key_value = ""
    bib_dict_arr = []
    bib_dict = {}
    for t in text:
        # section controll
        if t == "{":
            section += 1
            if section == 1: continue
        if t == "}":
            section -= 1
            if section == 0: continue

        # check the name
        if t == "{" and section == 0:
            published = (key_name.upper() == "@ARTICLE")
            key_name = ""
            continue

        # last }
        if t == "}" and section == -1:
            bib_dict[key_name.lower()] = key_value
            if published : bib_dict_arr.append(bib_dict.copy())
            bib_dict = {}

        # skip the blank and change line
        if t == " "  and section <= 0: continue
        if t == "\n" and section <= 0: continue

        # check the section
        if t == "{" and section == 0:
            store_key = True
            continue

        if t == "}" and section == -1:
            store_to_dict = True

        if t == "=" and section == 0:
            store_key = False
            continue

        if t == "," and section == 0:
            store_to_dict = True

        # store the value
        if store_to_dict:
            store_to_dict = False
            store_key = True
            bib_dict[key_name.lower()] = key_value
            key_name = ""
            key_value = ""
            continue

        # collect text
        if store_key:
            key_name += t
        else:
            key_value += t

    bib_arr = [ bibtex(bib_dict) for bib_dict in bib_dict_arr ]

    return bib_arr



#====================================================================================================
# Main
#====================================================================================================
if __name__ == "__main__":
    parser = argparse.ArgumentParser( prog="python3 bib2html.py",
                                      description="Transform the .bib information to html content",
                                      epilog = "")

    parser.add_argument('filename', nargs="+", help="The bibtex files")
    args = parser.parse_args()

    for file in args.filename:
        bib_arr = text2bibtex( file )
        for B in bib_arr:
            B.generate_html()
