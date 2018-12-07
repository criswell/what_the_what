#! /usr/bin/env python

from fuzzysearch import find_near_matches

# 2018-12-07 16:12:44.930894
lines = []

# 2018-12-07 16:12:47.735915
with open('delme.txt') as f:
    for line in f:
        if not lines:
            lines = []
        lines.append(line.strip())

# 2018-12-07 16:13:16.474723
full_text = ''.join(lines)

def show_subs(text, n):
    matches = find_near_matches(text, full_text, max_l_dist=n)
    print(matches)
    for m in matches:
        print("({0}:{1}) '{2}'".format(m.start, m.end, full_text[m.start:m.end]))


# 2018-12-07 16:21:53.030168
print(1)
show_subs('bumpy roadster of fire', 1)

# 2018-12-07 16:21:54.859264
print(2)
show_subs('bumpy roadster of fire', 2)

# 2018-12-07 16:21:57.193657
print(3)
show_subs('bumpy roadster of fire', 3)

# 2018-12-07 16:22:07.435338
print(4)
show_subs('bumpy roadster of fire', 4)

# 2018-12-07 16:22:10.907444
print(5)
show_subs('bumpy roadster of fire', 5)

# 2018-12-07 16:22:13.999431
print(10)
show_subs('bumpy roadster of fire', 10)
