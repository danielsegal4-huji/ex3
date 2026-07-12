# Part (c) - print a list of the top 20 tokens
# Owner: Member 1

from collections import Counter
from common import load_book, get_tokens

text = load_book()
tokens = get_tokens(text)
counts = Counter(tokens)

top20 = counts.most_common(20)

# print the list and also save it to a file so it can be copied into the report
with open("../output/part_c_top20.txt", "w", encoding="utf-8") as f:
    f.write("top 20 tokens:\n")
    for token, count in top20:
        line = token + " " + str(count)
        print(line)
        f.write(line + "\n")
