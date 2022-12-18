import requests
from bs4 import BeautifulSoup
import csv
url = "https://www.brainyquote.com/topics/motivational-quotes"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html5lib")

quotes=[]
table = soup.find("div", attrs = {"id":"quotelist"})
for row in table.find("div", attrs = {"class" : "qti-listm"}):
    quote = {} # We fill this in a loop
    try:
        quote["author"] = row.img["alt"].split("-")[1]
        quote["text"] = row.img["alt"].split("-")[0]
        quotes.append(quote)
        print(quote)
    except TypeError:
        continue
fileName = "short_quotes.csv"
with open(fileName, "w", newline="") as f:
    w = csv.DictWriter(f,["author","text"])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)