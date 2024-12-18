import gzip 
import sys 
import urllib
from urllib.parse import unquote_plus

# gzcat 20160602/* | python3 mapper.py > map_20160602_output.txt
# cat map_20160601_output.txt map_20160602_output.txt | LC_ALL=C sort -k 1 |
# cat mapper_output.txt | python3 reducer.py > reducer_output.txt


excluded_pagenames = [
    "Media", "Special", "Talk", "User", "User_talk", "Project",
    "Project_talk", "File", "File_talk", "MediaWiki",
    "MediaWiki_talk", "Template", "Template_talk", "Help", "Help_talk",
    "Category", "Category_talk", "Portal", "Wikipedia", "Wikipedia_talk"
]

file_extensions = [
    "jpg", "gif", ".png", ".JPG", ".GIF", ".PNG", ".ico", ".txt"
]

excluded_boilerplates = names = [
    "404_error", "Main_Page", "Hypertext_Transfer_Protocol", 
    "Favicon.ico", "Search"
]

def filter(line):
    stripped_line = line.strip()
    project_code, page_name, pageviews, bytes = stripped_line.split()
    # Step 1
    filtered_page_name = unquote_plus(page_name)
    # filtered_page_name = filtered_page_name.strip()
    # filtered_page_name = filtered_page_name.replace("\n", " ")
    # Step 2
    if project_code != "en":
        return None
    # Step 3
    for excluded in excluded_pagenames:
        if filtered_page_name.startswith(excluded):
            return None
    # Step 4
    if all(ord(c) < 128 for c in page_name[0]) and page_name[0].isalpha() and page_name[0].islower():
        return None 
    # Step 5
    for ext in file_extensions:
        if filtered_page_name.endswith(ext):
            return None
    # Step 6
    for boilerplate in excluded_boilerplates:
        if boilerplate in filtered_page_name:
            return None

    return filtered_page_name + "\t" + pageviews
    
for line in sys.stdin:
    filtered_line = filter(line)
    if filtered_line:
        print(filtered_line)


