Text Mining assignment - The Travels of Marco Polo, Volume 1 (Gutenberg #10636)

How to run
----------
Requirements: python 3, nltk, matplotlib, wordcloud (for part g).
    pip install nltk matplotlib wordcloud

Run each part from inside the code/ folder, for example:
    cd code
    python part_b.py

The scripts read the book from ../pg10636.txt and save plots to ../output/.
nltk downloads the models it needs on the first run.

Files
-----
common.py  - shared helpers (load_book, get_tokens, plot_zipf), used by b/c/d/e
part_b.py  - (b) tokenize, count, log-log frequency vs rank plot   [Member 1, done]
part_c.py  - (c) top 20 tokens                                     [Member 1]
part_d.py  - (d) repeat (b) without stopwords                      [Member 1]
part_e.py  - (e) repeat (b) with stemming + comparison writeup     [Member 2]
part_f.py  - (f) a POS tagging mistake + explanation               [Member 2]
part_g.py  - (g) proper-noun (NNP/NNPS) tag cloud                  [Member 3]
part_h.py  - (h) regex for two consecutive repeated words          [Member 3]

Part (a) - the book name - goes in the report only, no code needed.
