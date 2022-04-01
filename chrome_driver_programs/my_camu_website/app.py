from selenium import webdriver
from parsers.my_camu_parser import My_Camu_Parser

chrome = webdriver.Chrome(executable_path="/Users/ulaganathan/Software/ChromeDriver/chromedriver")
chrome.maximize_window()
chrome.get("https://www.mycamu.co.in/#/")

my_camu_parser_obj = My_Camu_Parser(chrome)

my_camu_parser_obj.typing_username()
my_camu_parser_obj.typing_password()
my_camu_parser_obj.login_button.click()
# my_camu_parser_obj.time_table_button.click()
