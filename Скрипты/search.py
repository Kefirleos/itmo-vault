import urllib.request, urllib.parse
from html.parser import HTMLParser
import sys

class DDGParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_result = False
        self.in_title = False
        self.in_snippet = False
        self.current_title = []
        self.current_snippet = []
        self.current_link = ""
        self.results = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and "class" in attrs and "result__url" in attrs["class"]:
            self.current_link = attrs.get("href", "")
        if tag == "h2" and "class" in attrs and "result__title" in attrs["class"]:
            self.in_title = True
        if tag == "a" and "class" in attrs and "result__snippet" in attrs["class"]:
            self.in_snippet = True

    def handle_endtag(self, tag):
        if tag == "h2" and self.in_title:
            self.in_title = False
        if tag == "a" and self.in_snippet:
            self.in_snippet = False
            self.results.append({
                "title": "".join(self.current_title).strip(),
                "link": self.current_link.strip(),
                "snippet": "".join(self.current_snippet).strip()
            })
            self.current_title = []
            self.current_snippet = []
            self.current_link = ""

    def handle_data(self, data):
        if self.in_title:
            self.current_title.append(data)
        if self.in_snippet:
            self.current_snippet.append(data)

def search(query):
    q = urllib.parse.quote(query)
    req = urllib.request.Request(
        f'https://html.duckduckgo.com/html/?q={q}', 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    )
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        parser = DDGParser()
        parser.feed(html)
        for i, r in enumerate(parser.results):
            print(f"[{i+1}] {r['title']}\n    Link: {r['link']}\n    Snippet: {r['snippet']}\n")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    search(sys.argv[1])
