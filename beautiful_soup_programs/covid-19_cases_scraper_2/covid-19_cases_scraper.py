import requests
from bs4 import BeautifulSoup

page_content = requests.get("https://news.google.com/covid19/map?hl=en-IN&gl=IN&ceid=IN%3Aen").content
soup = BeautifulSoup(page_content, "html.parser")

locater = "div.pcAJd"
table_locater = soup.findAll('div', {"class" : "pcAJd"})

for country in table_locater:
    print(country)
print(len(table_locater))
