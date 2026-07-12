# Shared helpers used by several parts (b, c, d, e).
# Import from here so we don't repeat the tokenizing / plotting code.

import nltk
from collections import Counter
import matplotlib.pyplot as plt

# nltk needs the tokenizer models, download them once
nltk.download("punkt")
nltk.download("punkt_tab")

BOOK_PATH = "../pg10636.txt"


def load_book(path=BOOK_PATH):
    """Read the book file and return only the text, without the Gutenberg header/footer."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    # cut off the Project Gutenberg header and footer so we only keep the book itself
    start = text.index("*** START")
    start = text.index("\n", start)  # skip to the end of the start marker line
    end = text.index("*** END")
    return text[start:end]


def get_tokens(text):
    """Tokenize the text into lowercase words (punctuation and numbers dropped)."""
    tokens = nltk.word_tokenize(text.lower())
    tokens = [t for t in tokens if t.isalpha()]  # keep words only, drop punctuation and numbers
    return tokens


def plot_zipf(counts, title, filename):
    """Plot token frequency vs rank on log-log axes and save the figure to filename."""
    freqs = sorted(counts.values(), reverse=True)
    ranks = range(1, len(freqs) + 1)
    plt.figure()
    plt.loglog(ranks, freqs)
    plt.title(title)
    plt.xlabel("rank (log scale)")
    plt.ylabel("frequency (log scale)")
    plt.savefig(filename)
