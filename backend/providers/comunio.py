from html.parser import HTMLParser
from urllib.request import Request, urlopen
import re

URL = "https://stats.comunio.de/"

def money(value):
    digits = re.sub(r"[^0-9]", "", value or "")
    return int(digits) if digits else None

class TableParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.in_row=False; self.cells=[]; self.rows=[]; self.in_cell=False; self.buf=[]
    def handle_starttag(self, tag, attrs):
        if tag == "tr": self.in_row=True; self.cells=[]
        elif self.in_row and tag in ("td","th"): self.in_cell=True; self.buf=[]
    def handle_data(self, data):
        if self.in_cell: self.buf.append(data)
    def handle_endtag(self, tag):
        if tag in ("td","th") and self.in_cell:
            self.cells.append(re.sub(r"\s+", " ", "".join(self.buf)).strip()); self.in_cell=False
        elif tag == "tr" and self.in_row:
            if self.cells: self.rows.append(self.cells)
            self.in_row=False

def fetch_values():
    req = Request(URL, headers={"User-Agent":"FantasyScout/1.0"})
    with urlopen(req, timeout=20) as r: raw=r.read()
    p=TableParser(); p.feed(raw.decode("utf-8","ignore"))
    result={}
    for row in p.rows:
        if len(row) < 3: continue
        name=row[0]
        # Find the first plausible euro amount in the row.
        value=next((money(c) for c in row[1:] if "€" in c or re.search(r"\d[\d.]*", c)), None)
        if name and value: result[normalize(name)] = value
    return result

def normalize(value):
    import unicodedata
    value=unicodedata.normalize("NFKD",value).encode("ascii","ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+","",value)
