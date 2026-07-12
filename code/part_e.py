# Part (e) - repeat part (b) with stemmed text
# Owner: Member 2

from collections import Counter
from nltk.stem import PorterStemmer
from common import load_book, get_tokens, plot_zipf


def stem_tokens(tokens):
    # TODO: stem every token using PorterStemmer and return the stemmed list.
    pass


text = load_book()
tokens = get_tokens(text)

# TODO: stem the tokens, count them, and plot the log-log graph
#       save it to ../output/part_e_zipf.png

# TODO (for the report): write 3-4 sentences explaining how the counts change
#       between the original tokens (b), after removing stopwords (d),
#       and after stemming (e).
