import requests
from bs4 import BeautifulSoup

page_content = requests.get("https://example.com/").content

soup = BeautifulSoup(page_content, "html.parser")

heading = soup.select_one("h1").string
content = soup.select_one("p").string.strip()
link = soup.select_one("a").attrs['href']

print(f"Heading ---- {heading}")
print(f"Content ---- {content}")
print(f"Link ---- {link}")
