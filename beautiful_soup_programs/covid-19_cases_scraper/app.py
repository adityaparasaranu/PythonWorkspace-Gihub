import requests
from locaters.country_locater import CountryLocaters
from parsers.country_parser import CountryParser

page_content = requests.get("https://news.google.com/covid19/map?hl=en-IN&gl=IN&ceid=IN%3Aen&mid=%2Fm%2F09c7w0").content

country_parser = CountryParser(page_content)

country_name_list = []
# for country in country_parser.country_name(CountryLocaters.COUNTRY_NAME):
#     if country.string != "Worldwide":
#         country_name_list.append(country.string)

total_cases_list = []

count = 0
for total_cases in country_parser.total_cases(CountryLocaters.TOTAL_CASES):
    if count == 1:
        print(total_cases.string)
    count = 1
