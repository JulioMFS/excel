#import d as d
import requests
from bs4 import BeautifulSoup
import pandas as pd

user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.37"
page = requests.get(f'https://www.accuweather.com/pt/pt/chamusca/275494/daily-weather-forecast/275494', headers={'User-Agent': user_agent})
print(page.status_code)
soup = BeautifulSoup(page.content, "html.parser")
#print(soup.prettify())
seven_day = soup.find(class_="content-module")
print("7777: ",seven_day.contents)
forecast_items = seven_day.find_all(class_="daily-wrapper")
#---------------------------------------------------------
header_tag = soup.find(class_='content-module')
header_row = header_tag.children
data_row  = header_row.fetchNextSiblings('div')
for cell in data_row.find_all('div'):
    print(cell.text.strip())
#---------------------------------------------------------
tonight = forecast_items[0]
print(tonight.prettify())
period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()
print("<---------------->")
print(period)
print(short_desc)
print(temp)
print("<------img---------->")
img = tonight.find("img")
desc = img["title"]
print(desc)
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
print("<------periods---------->")
print(periods)
short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]
print("--> short_descs: ", short_descs)
print("--> temps:", temps)
print("--> descs: ", descs)

weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc": descs
})
weather
print("<---------weather----->")
print(weather)
temp_nums = weather["temp"].str.extract("(\d+)", expand=False)
weather["temp_num"] = temp_nums.astype("int")
print(temp_nums)
print(weather["temp_num"].mean())

is_night = weather["temp"].str.contains("Low")
weather["is_night"] = is_night
print("--> is_night", is_night)

print("+-----------------------------------------------------------------------------------------------------------------+")
print("+     This is the tutorial website: ", "https://www.dataquest.io/blog/web-scraping-python-using-beautiful-soup/", "     +")
print("+-----------------------------------------------------------------------------------------------------------------+")