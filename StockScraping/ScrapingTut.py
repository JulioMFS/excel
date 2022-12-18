from bs4 import BeautifulSoup
import requests
page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
print(page.status_code)
soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())
print("--> list(soup.children\n", list(soup.children))
print("--> [type(item) for item in list(soup.children)]\n", [type(item) for item in list(soup.children)])
html = list(soup.children)[2]
print ("--> html.children\n", html.children)
body = list(html.children)[3]
print("--> list(body.children\n", list(body.children))

from bs4 import BeautifulSoup
import requests
page = requests.get("https://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content, 'html.parser')
print("--> soup: \n", soup)
print("--> soup.find_all('p', class_='outer-text': \n",  soup.find_all('p', class_='outer-text'))
print("--> soup.find_all(id='first'): \n",  soup.find_all(id='first'))
print("--> soup.select('div p'): \n",  soup.select('div p'))