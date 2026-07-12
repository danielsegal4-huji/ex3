# Part (f) - show one example sentence where POS tagging made a mistake
# Owner: Member 2

import nltk

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("averaged_perceptron_tagger_eng")

# A real sentence taken from the book (The Travels of Marco Polo, Vol. 1).
sentence = "The remainder, however, is favourable to agriculture, and produces everything abundantly."

tokens = nltk.word_tokenize(sentence)
tags = nltk.pos_tag(tokens)

print("Sentence:")
print(" ", sentence)
print("\nPOS tags:")
for word, tag in tags:
    print(f"  {word:<12} {tag}")

# The mistake: "agriculture" is tagged VB (a base-form verb) but it is really a
# common noun (NN) - the object of the preposition "to".
print("\nMistake:")
print('  "agriculture" was tagged VB (verb) but it should be NN (noun).')

explanation = (
    'POS tagging mistake (part f)\n'
    'Sentence: "The remainder, however, is favourable to agriculture, and produces '
    'everything abundantly."\n\n'
    'The word "agriculture" is tagged VB (base-form verb), but it is actually a '
    'common noun (NN): it is the object of the preposition "to" in the phrase '
    '"favourable to agriculture".\n\n'
    'Why the tagger is fooled: the token "to" is by far most often the infinitive '
    'marker, which is normally followed by a base-form verb (e.g. "to run", "to '
    'go"). The averaged-perceptron tagger leans heavily on the previous tag, so '
    'after seeing "to" (tagged TO) it strongly prefers a following VB and overrides '
    'the fact that "agriculture" is only ever a noun. Here "to" is really a '
    'preposition, so the correct tag is NN.'
)

with open("../output/part_f_pos_error.txt", "w", encoding="utf-8") as f:
    f.write(explanation + "\n")