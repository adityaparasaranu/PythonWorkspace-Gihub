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


def all_laptops():
    for i in range(len(laptop_name_list)):
        print(f"Laptop : {laptop_name_list[i]}")
        print(f"Price : Rs. {laptop_price_list[i]}")
        print(f"Rating : {laptop_rating_list[i]}")
        print("")


def best_laptops():
    num = 4.5
    try:
        num = float(input("Enter an Rating to sort the Laptops with that Rating: "))
    except ValueError:
        print("")
        print("You have Given a Wrong Value in the place of Rating. Pls try again !")
        print("The rating as been taken as 4.5 as Default Value and has been displayed !")
        print("")

    for i in range(len(laptop_name_list)):
        if float(laptop_rating_list[i]) >= num:
            print(f"Laptop : {laptop_name_list[i]}")
            print(f"Price : Rs. {laptop_price_list[i]}")
            print(f"Rating : {laptop_rating_list[i]}")
            print("")


def cheapest_laptops():
    num = 60000
    try:
        num = int(input("Enter a Price without commas to sort the Laptops with that Price: "))
    except ValueError:
        print("")
        print("You have Given a Wrong Value in the place of Price. Pls try again !")
        print("The Price as been taken as 60000 as Default Value and has been displayed !")
        print("")

    for i in range(len(laptop_name_list)):
        if int(laptop_price_list[i]) <= num:
            print(f"Laptop : {laptop_name_list[i]}")
            print(f"Price : Rs. {laptop_price_list[i]}")
            print(f"Rating : {laptop_rating_list[i]}")
            print("")
