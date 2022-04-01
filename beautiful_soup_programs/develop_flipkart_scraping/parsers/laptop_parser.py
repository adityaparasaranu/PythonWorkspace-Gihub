from bs4 import BeautifulSoup


class LaptopParser:
    def __init__(self, page_content):
        """
        This creates an obj of Beautiful Soup
        and get an parameter called page content
        and provides that to the soup as an
        argument
        """
        self.soup = BeautifulSoup(page_content, "html.parser")

    def laptop_name(self, name_locater):
        """
        This would return a list of div tags
        where the laptop name would be inside it
        """
        return self.soup.select(name_locater)

    def laptop_price(self, price_locater):
        """
        This would return list of div tags
        where the laptop price would be inside
        it
        """
        return self.soup.select(price_locater)

    def laptop_rating(self, rating_locater):
        """
        This would return list of div tags
        where the laptop rating would be inside
        it
        """
        return self.soup.select(rating_locater)

    def about_laptop(self, about_laptop_locater):
        """
        This would return a list of ul tags with
        which we can find data about the laptop
        with the li tag which is inside the ul tag
        """
        return self.soup.select(about_laptop_locater)
