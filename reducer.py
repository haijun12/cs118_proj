import sys
curr_name, curr_views = None, 0

for line in sys.stdin:
    name, views = line.split("\t")
    if name == curr_name:
        views += curr_views
    else:
        print(curr_name + "\t" + str(curr_views))
        curr_name, curr_views = name, views

print(curr_name + "\t" + str(curr_views))

