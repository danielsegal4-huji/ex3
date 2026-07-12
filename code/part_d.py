# Part (d) - repeat part (b) after removing stopwords
# Owner: Member 1

import nltk
from collections import Counter
from nltk.corpus import stopwords
from common import load_book, get_tokens, plot_zipf

nltk.download("stopwords")


def remove_stopwords(tokens):
    stops = set(stopwords.words("english"))  # use a set for faster lookup
    return [t for t in tokens if t not in stops]


text = load_book()
tokens = get_tokens(text)
tokens = remove_stopwords(tokens)
counts = Counter(tokens)

print("number of tokens after removing stopwords:", len(tokens))
print("number of unique tokens:", len(counts))

plot_zipf(counts, "Marco Polo - token frequency vs rank (no stopwords)", "../output/part_d_zipf.png")
