"""Part (b) - tokenize the book, count each token, and plot frequency vs rank (log-log)."""

from collections import Counter
from common import load_book, get_tokens, plot_zipf

text = load_book()
tokens = get_tokens(text)
counts = Counter(tokens)

print("number of tokens:", len(tokens))
print("number of unique tokens:", len(counts))

plot_zipf(counts, "Marco Polo - token frequency vs rank", "../output/part_b_zipf.png")
