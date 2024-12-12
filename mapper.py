import gzip 
import sys 
import urllib

excluded_pagenames = [Media, Special, Talk, User, User_talk, Project,
Project_talk, File,File_talk, MediaWiki,
MediaWiki_talk, Template, Template_talk, Help, Help_talk, Category, Category_talk,
Portal, Wikipedia,Wikipedia_talk]
def filter(line):
    tokens = line.split()
    project = tokens[0]
    page_name = tokens[1]
    page_num = tokens[2]
    if project != "en":
        return None
    if page_name.tartswith()is_upper

    project_code, pagename, pageviews, bytes = line.split(" ")
    step_1 = urllib.unquote_plus(pagename)
    step_2 = project_code == "en"
    return filtered_line
    
for line in sys.stdin:
    filtered_line = filter(line)
    if filtered_line:
        print(filtered_line)


