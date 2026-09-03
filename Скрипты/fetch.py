import urllib.request, re
from bs4 import BeautifulSoup

def fetch(url, out_name):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        with open(out_name, 'w', encoding='utf-8') as f:
            f.write(soup.get_text(separator='\n', strip=True))
    except Exception as e:
        print(f"Error {url}: {e}")

fetch('https://faq.itmo.is/before/entry_test', 'entry_test.txt')
fetch('https://abit.itmo.ru/program/bachelor/software_engineering', 'program.txt')
