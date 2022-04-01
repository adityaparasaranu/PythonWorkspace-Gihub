from selenium.webdriver.support.ui import Select
from chrome_driver_programs.ncert_website.locaters.locaters import NcertLocaters


class Ncert_Parser :
    def __init__(self, browser):
        self.browser = browser

    @property
    def class_dropdown(self):
        element = self.browser.find_element_by_css_selector(NcertLocaters.CLASS_LOCATER)
        return Select(element)

    def select_class_name(self, class_name):
        self.class_dropdown.select_by_visible_text(class_name)

    @property
    def subject_dropdown(self):
        element = self.browser.find_element_by_css_selector(NcertLocaters.SUBJECT_LOCATER)
        return Select(element)

    def select_subject_name(self, subject_name):
        self.subject_dropdown.select_by_visible_text(subject_name)

    @property
    def book_dropdown(self):
        element = self.browser.find_element_by_css_selector(NcertLocaters.BOOK_LOCATER)
        return Select(element)

    def select_book_name(self, book_name):
        self.book_dropdown.select_by_visible_text(book_name)

    @property
    def class_options(self):
        options = [option.text.strip() for option in self.class_dropdown.options]

        class_option = ["", "Class Options: "]

        for option in options:
            if option == "..Select Class.." or option == "":
                pass

            else:
                class_option.append(option)

        class_option.append("")

        return class_option


    @property
    def subject_options(self):
        options = [option.text.strip() for option in self.subject_dropdown.options]

        subject_option = ["", "Subject Options : "]

        for option in options:
            if option == "..Select Subject.." or option == "":
                pass

            else:
                subject_option.append(option)

        subject_option.append("")

        return subject_option

    @property
    def book_name_options(self):
        options = [option.text.strip() for option in self.book_dropdown.options]

        book_option = ["", "Book Options: "]

        for option in options:
            if option == "..Select Book Title.." or option == "":
                pass

            else:
                book_option.append(option)

        book_option.append("")

        return book_option

    @property
    def go_button(self):
        return self.browser.find_element_by_css_selector(NcertLocaters.GO_BUTTON_LOCATER)

    @property
    def download_button(self):
        self.browser.find_element_by_link_text("Download complete book ")

