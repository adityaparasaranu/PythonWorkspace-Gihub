from selenium.webdriver.support.ui import Select

from chrome_driver_programs.my_camu_website.locaters.my_camu_locaters import My_Camu_Locaters

class My_Camu_Parser:
    def __init__(self, browser):
        self.browser = browser

    def typing_username(self, username= "kgomathisankari@yahoo.co.in"):
        element = self.browser.find_element_by_css_selector(My_Camu_Locaters.USER_NAME_LOCATER)
        element.send_keys(username)

    def typing_password(self, password= "aravind"):
        element = self.browser.find_element_by_css_selector(My_Camu_Locaters.PASSWORD_LOCATER)
        element.send_keys(password)

    @property
    def login_button(self):
        return self.browser.find_element_by_css_selector(My_Camu_Locaters.LOGIN_BUTTON_LOCATER)

    @property
    def time_table_button(self):
        return self.browser.find_element_by_css_selector(My_Camu_Locaters.TIME_TABLE_LOCATER)



