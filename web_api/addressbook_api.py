from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from web_api.session_helper import SessionHelper
from web_api.contact_helper import ContactHelper
from web_api.group_helper import GroupHelper

class AddressBookAPI:
    def __init__(self, browser, base_url):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "edge":
            self.wd = webdriver.Edge()
        else:
            raise ValueError("Unrecognized browser {}".format(browser))
        # self.wd = webdriver.Firefox()
        # self.wd.implicitly_wait(5)
        # self.session = SessionHelper(self)
        self.wd.implicitly_wait(5)
        self.base_url=base_url
        self.session=SessionHelper(self)
        self.contact=ContactHelper(self)
        self.group=GroupHelper(self)


    def open_home_page(self):
        wd = self.wd
        # Open home page
        wd.get(self.base_url)


    def is_element_present(self, by, locator):
        wd = self.wd
        try:
            wd.find_element(by, locator)
            return True
        except NoSuchElementException:
            return False

    def find_message(self):
        wd = self.wd
        return wd.find_element_by_css_selector("div.msgbox").text

    def destroy(self):
        self.wd.quit()
