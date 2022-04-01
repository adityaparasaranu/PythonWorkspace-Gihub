from selenium import webdriver
from paresrs.ncert_parsers import Ncert_Parser

chrome = webdriver.Chrome(executable_path="/Users/ulaganathan/Software/ChromeDriver/chromedriver")
chrome.get("https://ncert.nic.in/textbook.php")

ncert_parser_obj = Ncert_Parser(chrome)

for classes in ncert_parser_obj.class_options:
    print(classes)

class_name_input = input("Enter the Class : ")
ncert_parser_obj.select_class_name(class_name_input)

for subject in ncert_parser_obj.subject_options:
    print(subject)

subject_input = input("Enter the Subject : ").strip().lower().capitalize()
ncert_parser_obj.select_subject_name(subject_input)

for book in ncert_parser_obj.book_name_options:
    print(book)

book_name = input("Enter the Book Name : ").strip().lower().capitalize()
ncert_parser_obj.select_book_name(book_name)

ncert_parser_obj.go_button.click()
print("")
print("Success")
print("The Button is Clicked...")

ncert_parser_obj.download_button.click()
