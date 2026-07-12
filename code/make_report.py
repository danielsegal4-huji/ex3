
# Assemble the consolidated report PDF for the Text Mining assignment.
# Owner: Member 2
#
# Collects every required output (plots, top-20 list, POS example, tag cloud,
# regex + matches and the written explanations) into one PDF in ../output/.
# Parts that have not been produced yet (e.g. Member 3's g/h outputs) are shown
# as clearly-marked placeholders so the report still builds.
#
# Requires: reportlab  (pip install reportlab)

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak,
)

OUTPUT_DIR = "../output"
REPORT_PATH = os.path.join(OUTPUT_DIR, "report.pdf")

BOOK_NAME = "The Travels of Marco Polo, Volume 1 (Project Gutenberg eBook #10636)"

# Group 53 - project 67978 "A Needle in a Data Haystack"
GROUP_NUMBER = "53"
MEMBERS = [
    # (Full name, Teudat Zehut, CSE username, University email)
    ("Tal Raiter", "208997908", "talraiter", "tal.raiter@mail.huji.ac.il"),
    ("Tomer Kadosh", "209460005", "tomer_kadosh", "Tomer.kadosh@mail.huji.ac.il"),
    ("Daniel Segal", "316368240", "danielsegalr", "daniel.segal4@mail.huji.ac.il"),
    ("Moshe Ohana", "315742692", "moshe.ohana", "moshe.ohana@mail.huji.ac.il"),
]

styles = getSampleStyleSheet()
H1 = styles["Heading1"]
H2 = styles["Heading2"]
BODY = styles["BodyText"]
TITLE = ParagraphStyle("BigTitle", parent=styles["Title"], fontSize=20, leading=24)
CENTER = ParagraphStyle("Center", parent=BODY, alignment=TA_CENTER)
MONO = ParagraphStyle("Mono", parent=BODY, fontName="Courier", fontSize=9, leading=12)
MISSING = ParagraphStyle("Missing", parent=BODY, textColor=colors.red)


def read_text(name, fallback):
    """Read a text file from output/ or return a fallback placeholder string."""
    path = os.path.join(OUTPUT_DIR, name)
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return f.read().strip()
    return fallback


def add_image(story, name, width=15 * cm):
    """Add an image from output/ scaled to `width`, or a red placeholder line."""
    path = os.path.join(OUTPUT_DIR, name)
    if os.path.exists(path):
        img = Image(path)
        ratio = img.imageHeight / float(img.imageWidth)
        img.drawWidth = width
        img.drawHeight = width * ratio
        story.append(img)
    else:
        story.append(Paragraph(
            f"[ MISSING: {name} - run the part that produces it, then rebuild ]",
            MISSING))
    story.append(Spacer(1, 0.4 * cm))


def para(story, text, style=BODY, gap=0.3 * cm):
    for block in text.split("\n\n"):
        story.append(Paragraph(block.replace("\n", "<br/>"), style))
        story.append(Spacer(1, gap))


story = []

# ---- Title page ----
story.append(Spacer(1, 3 * cm))
story.append(Paragraph("Text Mining Assignment - Report", TITLE))
story.append(Spacer(1, 0.6 * cm))
story.append(Paragraph(f"Group {GROUP_NUMBER}", CENTER))
story.append(Spacer(1, 0.3 * cm))
story.append(Paragraph(f"Book: {BOOK_NAME}", CENTER))
story.append(Spacer(1, 1.0 * cm))

member_rows = [["Full name", "Teudat Zehut", "CSE username", "University email"]]
member_rows += [list(m) for m in MEMBERS]
tbl = Table(member_rows, colWidths=[3.5 * cm, 3 * cm, 3 * cm, 6 * cm])
tbl.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#4472C4")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTSIZE", (0, 0), (-1, -1), 8),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#EAF0FB")]),
]))
story.append(tbl)
story.append(PageBreak())

# ---- (a) Book name ----
story.append(Paragraph("(a) Book", H1))
para(story, f"The chosen book is <b>{BOOK_NAME}</b>.")

# ---- (b) Frequency vs rank ----
story.append(Paragraph("(b) Token frequency vs rank (log-log)", H1))
para(story, "The book was tokenized into lowercase word tokens (punctuation and "
            "numbers dropped) and each token counted. The plot below shows token "
            "frequency against rank on log-log axes - the near-straight line is the "
            "signature of Zipf's law.")
add_image(story, "part_b_zipf.png")
story.append(PageBreak())

# ---- (c) Top 20 tokens ----
story.append(Paragraph("(c) Top 20 tokens", H1))
top20 = read_text("part_c_top20.txt", "[ MISSING: part_c_top20.txt ]")
para(story, top20, MONO)
story.append(PageBreak())

# ---- (d) Without stopwords ----
story.append(Paragraph("(d) Frequency vs rank without stopwords", H1))
para(story, "The same analysis after removing English stopwords. Removing the "
            "closed set of very frequent function words strips the top of the "
            "ranking, leaving content words.")
add_image(story, "part_d_zipf.png")
story.append(PageBreak())

# ---- (e) Stemming ----
story.append(Paragraph("(e) Frequency vs rank with stemming", H1))
para(story, "The tokens were reduced to their stems with the Porter stemmer, then "
            "counted and plotted on log-log axes.")
add_image(story, "part_e_zipf.png")
comparison = read_text("part_e_comparison.txt", "[ MISSING: part_e_comparison.txt ]")
story.append(Paragraph("Comparison (original / no-stopwords / stemmed):", H2))
para(story, comparison)
story.append(PageBreak())

# ---- (f) POS tagging mistake ----
story.append(Paragraph("(f) A POS tagging mistake", H1))
pos_err = read_text("part_f_pos_error.txt", "[ MISSING: part_f_pos_error.txt ]")
para(story, pos_err)
story.append(PageBreak())

# ---- (g) Proper-noun tag cloud ----
story.append(Paragraph("(g) Proper-noun (NNP/NNPS) tag cloud", H1))
para(story, "A tag cloud of the proper nouns in the book (case preserved). See the "
            "written explanation of whether it matches the book below.")
add_image(story, "part_g_cloud.png")
gexp = read_text("part_g_explanation.txt",
                 "[ TODO Member 3: paste the explanation of whether the tag cloud "
                 "matches the book. ]")
para(story, gexp)
story.append(PageBreak())

# ---- (h) Repeated-words regex ----
story.append(Paragraph("(h) Regex for two consecutive repeated words", H1))
hexp = read_text("part_h_matches.txt",
                 "[ TODO Member 3: paste the regular expression and the matches "
                 "it found. ]")
para(story, hexp, MONO)

doc = SimpleDocTemplate(
    REPORT_PATH, pagesize=A4,
    leftMargin=2 * cm, rightMargin=2 * cm, topMargin=2 * cm, bottomMargin=2 * cm,
    title="Text Mining Assignment - Report", author=f"Group {GROUP_NUMBER}",
)
doc.build(story)
print("wrote", REPORT_PATH)