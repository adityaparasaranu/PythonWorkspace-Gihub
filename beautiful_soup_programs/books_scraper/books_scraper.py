import requests
from bs4 import BeautifulSoup

page_content = requests.get("http://books.toscrape.com/").content

soup = BeautifulSoup(page_content, "html.parser")

books_names = []
books_prices = []
books_ratings = []

article_locater = "ol.row li.col-xs-6 article.product_pod h3 a"
books = soup.select(article_locater)

for book in books:
    book_name = book.attrs['title']
    books_names.append(book_name)

price_locater = "ol.row li.col-xs-6 article.product_pod div.product_price p.price_color"
prices = soup.select(price_locater)

for price in prices:
    book_price = price.string
    books_prices.append(book_price)

star_locater = "ol.row li.col-xs-6 article.product_pod p.star-rating"
star_ratings = soup.select(star_locater)

for star_rating in star_ratings:
    rating = star_rating.attrs['class']
    books_ratings.append(rating)

stock_locater = "ol.row li.col-xs-6 article.product_pod p.instock"
stocks = soup.select(stock_locater)

# for stock in stocks:
#     print(stock.string)
count = 1

for i in range(len(books_names)):
    print(f'{count}. Name ---- "{books_names[i]}"   Price ---- {books_prices[i]}   Rating ---- {books_ratings[i][1]}')
    count += 1

