import sys
import re

component_count = 0
the_word = ""
the_perm = ""
for i, line in enumerate(sys.stdin):
    if i == 0:
        the_word = line.strip()
    else:
        the_perm = line.strip()
for i in the_perm:
    if i in the_word:
        the_word = re.sub(fr'[{i}]', '', the_word)
        if len(the_word) == 0:
            print("WIN")
            break
    else:
        component_count += 1
        if component_count == 10:
            print("LOSE")
            break
