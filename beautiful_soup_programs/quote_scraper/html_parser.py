import requests
from bs4 import BeautifulSoup

page = requests.get("http://quotes.toscrape.com/")
soup = BeautifulSoup(page.content, "html.parser")

locator_for_quote = "body div.container div.row div.col-md-8 span.text"
locator_for_author = "body div.container div.row div.col-md-8 span small.author"

elements = soup.select(locator_for_quote)
authors = soup.select(locator_for_author)

for quote in elements:
    print(f"{elements.index(quote) + 1}. {quote.string} --- {authors[elements.index(quote)].string}")
