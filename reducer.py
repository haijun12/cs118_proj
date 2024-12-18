import sys
curr_name, curr_views = None, 0
word = None
lines_read = 0

for line in sys.stdin:
    stripped_line = line.strip()
    if (len(line.split("\t")) != 2):
        print(line, file=sys.stderr)
        continue
    word, views = stripped_line.split("\t", 1)
    views = int(views)
    if curr_name is None:
        curr_name = word
        curr_views += views
    elif word == curr_name:
        curr_views += views
    else:
        print(curr_name + "\t" + str(curr_views))
        curr_name, curr_views = word, views
    lines_read += 1

print(curr_name + "\t" + str(curr_views))

