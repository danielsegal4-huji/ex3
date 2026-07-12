# Part (h) - regex to find two consecutive repeated words (with possible punctuation between)
# Owner: Member 3

import re
from collections import Counter
from common import load_book

# \b([a-zA-Z]+) captures a word (letters only, so digits like "2, 2" and the
# underscores Gutenberg uses for italics don't count), [,.;:!?"']* allows
# punctuation right after it, \s+ is the whitespace between the words, and
# \1\b requires the same word again. re.IGNORECASE also catches "No, no".
pattern = r"\b([a-zA-Z]+)[,.;:!?\"']*\s+\1\b"

text = load_book()

matches = [" ".join(m.group(0).split()) for m in re.finditer(pattern, text, re.IGNORECASE)]
counts = Counter(m.lower() for m in matches)

print("regex:", pattern)
print("number of matches:", len(matches))
print()

# print the matches and save them to a file so they can be copied into the report
with open("../output/part_h_matches.txt", "w", encoding="utf-8") as f:
    f.write("regex: " + pattern + "\n")
    f.write("number of matches: " + str(len(matches)) + "\n\n")
    for match, count in counts.most_common():
        line = match + " (x" + str(count) + ")"
        print(line)
        f.write(line + "\n")
