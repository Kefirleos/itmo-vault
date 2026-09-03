import urllib.request, urllib.parse, json
import re

def ddg_search(query):
    print(f"Searching for: {query}")
    url = "https://html.duckduckgo.com/html/"
    data = urllib.parse.urlencode({'q': query}).encode('utf-8')
    req = urllib.request.Request(
        url, 
        data=data, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    )
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        results = re.findall(r'<a class="result__snippet[^>]*>(.*?)</a>', html, re.DOTALL | re.IGNORECASE)
        links = re.findall(r'<a class="result__url" href="([^"]+)">', html, re.DOTALL | re.IGNORECASE)
        titles = re.findall(r'<h2 class="result__title">.*?<a[^>]*>(.*?)</a>', html, re.DOTALL | re.IGNORECASE)
        for i in range(min(5, len(results))):
            snippet = re.sub(r'<[^>]+>', '', results[i]).strip()
            title = re.sub(r'<[^>]+>', '', titles[i]).strip() if i < len(titles) else ''
            link = links[i] if i < len(links) else ''
            print(f"[{i+1}] {title}\nURL: {link}\n{snippet}\n")
    except Exception as e:
        print(f"Error: {e}")

queries = [
    "ИТМО расшифровка групп первая буква",
    "ИТМО \"у30\" группа",
    "ИТМО факультет ИС",
    "ИТМО номер группы расшифровка",
    "ИТМО аббревиатура ИС"
]

with open("out_groups.txt", "w", encoding="utf-8") as f:
    import sys
    sys.stdout = f
    for q in queries:
        ddg_search(q)
