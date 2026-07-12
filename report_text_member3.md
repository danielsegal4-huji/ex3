# Member 3 - text for the consolidated report (parts g and h)

For Member 2: paste these into the report PDF next to the matching outputs.
This file is a working draft - it does not need to be in the submission zip.

## Part (g) - proper-noun tag cloud

Include the image: `output/part_g_cloud.png`

> The tag cloud of proper nouns (NNP/NNPS) matches the book very well. The most
> frequent proper nouns are Polo (820), Marco (650), Kaan (316), Khan (274) and
> Kublai (256) - the traveler himself and the Mongol emperor he served - together
> with the places on his route: China, India, Persia, Venice, Cathay, Hormuz and
> Tibet. Names like Yule, Pauthier and Ramusio also appear prominently because
> this Gutenberg edition includes extensive commentary by its translator Sir
> Henry Yule and refers to earlier editors, and those notes are part of the text.
> We filtered out all-caps tokens (from chapter headings like "THE TRAVELS OF...")
> and single letters (scholars' initials such as "H. Yule"), which the POS tagger
> mis-labels as proper nouns.

## Part (h) - regex for two consecutive repeated words

The regular expression (used with `re.IGNORECASE`):

    \b([a-zA-Z]+)[,.;:!?"']*\s+\1\b

> `\b([a-zA-Z]+)` captures a word, `[,.;:!?"']*` allows punctuation right after
> it, `\s+` matches the whitespace between the words, and `\1\b` requires the
> exact same word to appear again. Restricting the capture to letters keeps
> digits and the underscores Project Gutenberg uses for italics from producing
> false matches.
>
> It found 81 matches in the book, for example: "no, no", "had had" (x5),
> "long long", "thousand thousand", "you, you", "it, it" and "tuez, tuez".
> Many of the remaining matches are place names repeated across a sentence
> boundary (e.g. "Kerman. Kerman") and scholars' initials (e.g. the "H. H."
> in "H. H. Wilson"), which legitimately satisfy the pattern.

Include the full match list from: `output/part_h_matches.txt`
