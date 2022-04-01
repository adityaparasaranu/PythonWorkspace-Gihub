from selenium import webdriver
from PIL import Image

chrome = webdriver.Chrome(executable_path="/Users/ulaganathan/Software/ChromeDriver/chromedriver")
chrome.maximize_window()
chrome.get("https://www.mycamu.co.in/#/")

chrome.save_screenshot("/Users/ulaganathan/Aditya/screenshot.jpg")

screenshot = Image.open("/Users/ulaganathan/Aditya/screenshot.jpg")
screenshot.show()
