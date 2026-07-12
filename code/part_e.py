# Part (e) - repeat part (b) with stemmed text
# Owner: Member 2

from collections import Counter
from nltk.stem import PorterStemmer
from common import load_book, get_tokens, plot_zipf


def stem_tokens(tokens):
    # stem every token using PorterStemmer and return the stemmed list
    ps = PorterStemmer()
    return [ps.stem(t) for t in tokens]


text = load_book()
tokens = get_tokens(text)
stemmed = stem_tokens(tokens)
counts = Counter(stemmed)

print("number of tokens after stemming:", len(stemmed))
print("number of unique tokens:", len(counts))

plot_zipf(counts, "Marco Polo - token frequency vs rank (stemmed)", "../output/part_e_zipf.png")

# Comparison writeup (for the report) - saved so it can be pasted into the PDF.
# The exact numbers are filled in from the runs of parts (b), (d) and (e).
comparison = (
    "Comparison of token counts across parts (b), (d) and (e):\n"
    "Tokenizing the whole book gives {b_total} tokens made up of {b_unique} unique "
    "word types (part b). Removing English stopwords barely changes the number of "
    "unique types ({d_unique}) because stopwords are a small closed set of very "
    "frequent words, but it removes many token occurrences ({d_total} tokens left), "
    "which is why the top of the frequency ranking changes the most. Stemming with "
    "the Porter stemmer keeps the total number of tokens the same as in (b) "
    "({e_total}) but collapses inflected forms such as \"travel\", \"travels\" and "
    "\"travelling\" onto a single stem, cutting the vocabulary sharply to {e_unique} "
    "unique stems. As a result the stemmed frequencies are higher per type and the "
    "log-log Zipf curve stays straight but shifts left, since fewer distinct types "
    "now carry the same total mass."
)

# Fill in the numbers from the actual runs.
from nltk.corpus import stopwords
import nltk
nltk.download("stopwords")
stops = set(stopwords.words("english"))
no_stop = [t for t in tokens if t not in stops]

numbers = {
    "b_total": len(tokens),
    "b_unique": len(Counter(tokens)),
    "d_total": len(no_stop),
    "d_unique": len(Counter(no_stop)),
    "e_total": len(stemmed),
    "e_unique": len(counts),
}
comparison = comparison.format(**numbers)
print("\n" + comparison)

with open("../output/part_e_comparison.txt", "w", encoding="utf-8") as f:
    f.write(comparison + "\n")