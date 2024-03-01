#!/bin/python3

import argparse

#====================================================================================================
# Classes
#====================================================================================================
class bibtex():
    def __init__( self, bibtext_file ):
        bib_dict = self.text2dict( bibtext_file )
        self.title  = bib_dict.pop("title")
        self.author = self.clean_author( bib_dict.pop("author") )
        self.year   = bib_dict.pop("year")
        self.link   = bib_dict.pop("url")
        self.other  = bib_dict
        return

    def text2dict( self, file_name ):
        with open( file_name, "r" ) as f:
            text = ''.join( f.readlines() )

        start = False
        first_comma = True
        section = 0
        store_key = True
        key_name = ""
        key_value = ""
        bib_dict = {}
        for t in text:
            # skip until first {
            if t == "{" and not start:
                start = True
                continue
            if not start: continue

            # last }
            if t == "}" and section == 0:
                bib_dict[key_name.lower()] = key_value

            # skip the blank and change line
            if t == " "  and section == 0: continue
            if t == "\n" and section == 0: continue

            # check the section
            if t == "{":
                section += 1
                if section == 1: continue

            if t == "}":
                section -= 1
                if section == 0: continue

            if t == "=" and section == 0:
                store_key = False
                continue

            # store the value
            if t == "," and section == 0:
                # skip the first element in {}
                if first_comma:
                    first_comma = False
                    store_key = True
                    key_name = ""
                    key_value = ""
                else:
                    bib_dict[key_name.lower()] = key_value
                    store_key = True
                    key_name = ""
                    key_value = ""
                continue

            if store_key:
                key_name += t
            else:
                key_value += t

        return bib_dict

    def generate_html(self):
        # 1. title
        # 2. author
        # 3. link
        out_text  = ''
        out_text += '<li class="text-muted publication" data-tags="%s">\n'%self.year
        out_text += '    <div class="publication-title">\n'
        out_text += '        %s\n'%self.title
        out_text += '    </div>\n'
        out_text += '    <div class="publication-author">\n'
        out_text += '        %s\n'%self.author
        out_text += '    </div>\n'
        out_text += '    <div class="publication-link">\n'
        out_text += '        <a href="%s">link name</a>\n'%self.link
        out_text += '    </div>\n'
        out_text += '</li>'
        print(out_text)
        return out_text

    def clean_author(self, ugly_author):
        temp_author = ugly_author.split(" and ")
        out_author = []
        for author in temp_author:
            if "{" in author:
                temp = author.split("},")
                temp_author = temp[1] + " "+ temp[0][1:]
                out_author.append(temp_author)
            else:
                out_author.append(author)

        out_author[-1] = "and " + out_author[-1]
        return ", ".join(out_author)




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
        B = bibtex( file )
        B.generate_html()
