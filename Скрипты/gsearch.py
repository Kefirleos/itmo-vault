from googlesearch import search
import requests
from bs4 import BeautifulSoup
import sys
import re

queries = [
    "site:itmo.ru 09.03.02 Разработка программного обеспечения учебный план 1 курс языки дисциплины",
    "ИТМО ИС у30 расшифровка группы",
    "ИТМО распределительное тестирование первокурсников программирование английский математика формат",
    "ИТМО 09.03.02 Разработка программного обеспечения факультет мегафакультет"
]

def do_search():
    with open("out_utf8.txt", "w", encoding="utf-8") as f:
        for q in queries:
            f.write(f"=============================\nSearching for: {q}\n")
            try:
                urls = list(search(q, num_results=4, lang='ru'))
                for url in urls:
                    f.write(f"URL: {url}\n")
                    try:
                        resp = requests.get(url, timeout=5, headers={'User-Agent': 'Mozilla/5.0'})
                        soup = BeautifulSoup(resp.content, 'html.parser')
                        text = soup.get_text(separator=' ', strip=True)
                        text = re.sub(r'\s+', ' ', text)
                        f.write(f"Preview: {text[:1500]}...\n\n")
                    except Exception as e:
                        f.write(f"Error fetching {url}: {e}\n\n")
            except Exception as e:
                f.write(f"Search error: {e}\n")

if __name__ == "__main__":
    do_search()
