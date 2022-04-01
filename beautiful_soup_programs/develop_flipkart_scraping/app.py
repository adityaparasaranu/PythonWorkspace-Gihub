import requests
from bs4 import BeautifulSoup

from locaters.laptop_locater import LaptopLocater
from parsers.laptop_parser import LaptopParser

page_content = requests.get("https://www.flipkart.com/search?q=Best%20laptops&otracker=search&otracker1=search"
                            "&marketplace=FLIPKART&as-show=on&as=off").content
soup = BeautifulSoup(page_content, "html.parser")

laptop_parser = LaptopParser(page_content)

laptop_name_list = []

for laptop_name in laptop_parser.laptop_name(LaptopLocater.LAPTOP_NAME):
    laptop_name_list.append(laptop_name.string)

laptop_price_list = []

for laptop_price in laptop_parser.laptop_price(LaptopLocater.PRICE):
    laptop_price_list.append(laptop_price.string[1:].replace(",", ""))

laptop_rating_list = []

for laptop_rating in laptop_parser.laptop_rating(LaptopLocater.RATING):
    laptop_rating_list.append(laptop_rating.text)

about_laptop_list = []
nesting_list = []

for bullet_points in laptop_parser.about_laptop(LaptopLocater.ABOUT):
    for li in laptop_parser.about_laptop(f"{LaptopLocater.ABOUT} li.rgWa7D"):
        nesting_list.append(li.string)
    about_laptop_list.append(nesting_list)

# print(len(about_laptop_list))
# for i in about_laptop_list:
#     print(i)
#
print(len(about_laptop_list[0]))
print(f"    {about_laptop_list[0]}")


# print(len(laptop_name_list))


def all_laptops():
    for i in range(len(laptop_name_list)):
        print(f"Laptop : {laptop_name_list[i]}")
        print(f"Price : Rs {laptop_price_list[i]}")
        print(f"Rating : {laptop_rating_list[i]}")
        print("")


def best_laptops():
    for i in range(len(laptop_name_list)):
        if float(laptop_rating_list[i]) >= 4.0:
            print(f"Laptop : {laptop_name_list[i]}")
            print(f"Price : Rs {laptop_price_list[i]}")
            print(f"Rating : {laptop_rating_list[i]}")
            for j in range(len(laptop_name_list)):
                print(f"About the Laptop : {about_laptop_list[i]}")
            print("")


def cheapest_laptops():
    for i in range(len(laptop_name_list)):
        if int(laptop_price_list[i]) <= 60000:
            print(f"Laptop : {laptop_name_list[i]}")
            print(f"Price : Rs {laptop_price_list[i]}")
            print(f"Rating : {laptop_rating_list[i]}")
            print("")
