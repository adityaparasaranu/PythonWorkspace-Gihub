from bs4 import BeautifulSoup

class CountryParser:
    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, "html.parser")

    def country_name(self, country_locater):
        """
        This returns a list of all country names
        """
        return self.soup.select(country_locater)

    def total_cases(self, total_cases_locaters):
        """
        This returns a list where the total case will be
        in 0 element.
        """
        return self.soup.select(total_cases_locaters)

    def deadths(self, deadths_locaters):
        """
        This returns a list where the deadths will be
        3 element, 9 element and like so.
        """
        return self.soup.select(deadths_locaters)
