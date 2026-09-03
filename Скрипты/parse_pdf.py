import urllib.request
import pypdf
import os

url = "https://abitlk.itmo.ru/file_storage/academic_plan/2026/academic_plan_10328_09.03.02.pdf"
try:
    urllib.request.urlretrieve(url, "plan.pdf")
    reader = pypdf.PdfReader("plan.pdf")
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    with open("plan.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("PDF extracted successfully.")
except Exception as e:
    print("Error:", e)
