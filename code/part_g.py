# Part (g) - POS tag the text and make a tag cloud of the proper nouns (NNP, NNPS)
# Owner: Member 3

import nltk
from collections import Counter
from wordcloud import WordCloud
from common import load_book

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("averaged_perceptron_tagger_eng")


def get_proper_nouns(text):
    # NOTE: do NOT lowercase here - proper nouns need their original case and
    #       sentence context for the tagger to work, so tokenize the raw text.
    sentences = nltk.sent_tokenize(text)
    tokenized = [nltk.word_tokenize(s) for s in sentences]
    tagged = nltk.pos_tag_sents(tokenized)
    # skip single letters (initials like "H. Yule") and ALL-CAPS tokens (the
    # chapter headings, e.g. "THE", "NOTE", which the tagger mis-tags as NNP)
    return [word for sentence in tagged
            for word, tag in sentence
            if tag in ("NNP", "NNPS") and word.isalpha()
            and len(word) > 1 and not word.isupper()]


text = load_book()
proper_nouns = get_proper_nouns(text)
counts = Counter(proper_nouns)

print("number of proper noun occurrences:", len(proper_nouns))
print("number of unique proper nouns:", len(counts))
print("most common proper nouns:", counts.most_common(20))

cloud = WordCloud(width=1200, height=800, background_color="white")
cloud.generate_from_frequencies(counts)
cloud.to_file("../output/part_g_cloud.png")

# For the report: does the cloud match what you know about the book? explain.
# (The printed top-20 list above helps write the explanation.)
