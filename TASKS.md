# Work split - Text Mining assignment

Book: *The Travels of Marco Polo, Volume 1* (Project Gutenberg #10636).

Everyone imports the shared helpers from `code/common.py` (`load_book`, `get_tokens`,
`plot_zipf`). Use `code/part_b.py` as the example to copy the pattern from.
Each `.py` file has `TODO` markers showing exactly what to fill in.

---

## Member 1 - frequency pipeline + shared code
- **(a)** Write the book name in the report.
- **(b)** `part_b.py` - tokenize, count, and plot frequency vs rank (log-log).
- **(c)** `part_c.py` - print the top 20 tokens.
- **(d)** `part_d.py` - repeat (b) after removing stopwords, save the plot.
- Own `common.py` (the shared helpers everyone uses).

## Member 2 - stemming + POS errors + report PDF
- **(e)** `part_e.py` - repeat (b) with stemmed tokens, save the plot.
  Also write the 3-4 sentence comparison (original vs no-stopwords vs stemmed counts).
- **(f)** `part_f.py` - find one sentence where POS tagging is wrong, and explain the mistake.
- Assemble the consolidated report PDF (see the Report section below).

## Member 3 - proper nouns + regex
- **(g)** `part_g.py` - POS tag the text, make a tag cloud of proper nouns (NNP, NNPS),
  and explain whether it matches the book. (Do NOT lowercase - proper nouns need their case.)
- **(h)** `part_h.py` - write and run the regex for two consecutive repeated words,
  report the matches, and put the regex in the report.

---

## Report (goes in `output/`)
One consolidated PDF with: all group members' names + IDs, the book name, and every
required output (plots, the top-20 list, the POS example, the tag cloud, the regex + matches,
and the written explanations). All plots need a title and axis labels.
