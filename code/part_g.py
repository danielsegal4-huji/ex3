# Part (g) - POS tag the text and make a tag cloud of the proper nouns (NNP, NNPS)
# Owner: Member 3

import nltk
from collections import Counter
from common import load_book

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("averaged_perceptron_tagger_eng")


def get_proper_nouns(text):
    # NOTE: do NOT lowercase here - proper nouns need their original case and
    #       sentence context for the tagger to work, so tokenize the raw text.
    # TODO: tokenize the text, run nltk.pos_tag, and keep only words tagged NNP or NNPS.
    pass


text = load_book()
proper_nouns = get_proper_nouns(text)
counts = Counter(proper_nouns)

# TODO: build a tag cloud from the proper-noun counts and save it to
#       ../output/part_g_cloud.png
#       (you can use the `wordcloud` package, or an online tag-cloud tool as the
#        assignment allows - if online, paste the image into the report.)

# TODO (for the report): does the cloud match what you know about the book? explain.
