"""
A script replace the content between the start key and the end key.
Start key: <!--@@@REPLACE_KEY@@@-->
End   key: <!--$$$REPLACE_KEY$$$-->
"""
import re

def replace_section( filename, outname, content, keyword ):
    print( "Replacing content %20s: %30s => %30s"%(keyword, filename, outname) )
    start_key  = "<!--@@@" + keyword + "@@@-->"
    end_key    = "<!--$$$" + keyword + "$$$-->"

    with open(filename, 'r') as f:
        lines = f.readlines()

    write_mode = True
    #print(lines)  # clean the ' and " error
    with open(outname, 'w') as f:
        for num, line in enumerate(lines):
            if end_key in line: write_mode = True
            if not write_mode: continue
            f.write(line)
            if start_key in line:
                f.write(content)
                write_mode = False
    return

def get_latest_publication( filename, N ):
    pattern_start = 'class="text-muted publication"'
    pattern_end   = '</li>'

    with open( filename, 'r' ) as f:
        lines = f.readlines()

    target = []
    start = False
    cur_num = 0
    for line in lines:
        if pattern_start in line: start = True
        if not start: continue
        target.append(line)
        if pattern_end in line and start:
            start = False
            cur_num += 1
        if cur_num == N: break
    return ''.join(target)

if __name__ == "__main__":
    # get the common footer content
    with open( "common_html/footer.html", "r" ) as f:
        common_footer=f.read()

    # replace the footer section in the following files
    all_html = ["../index.html", "../teaching.html", "../members.html", "../publications.html", "../useful.html",
                "../news/2020.html", "../news/2021.html", "../news/2022.html", "../news/2023.html", "../news/2024.html"]
    for html in all_html:
        replace_section( html, html, common_footer, "FOOTER" )

    latest_pubs = get_latest_publication( "../publications.html", 3 )
    replace_section( "index.html", "index.htmlout", latest_pubs, "PUBLICATION" )
