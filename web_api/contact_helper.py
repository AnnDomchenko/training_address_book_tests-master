from models.contacts import Contact
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of

class ContactHelper:
    def __init__(self,app):
        self.app=app

    def is_contact_present(self):
        self.open_contact_page()
        return self.app.is_element_present(By.NAME, "selected[]")

    def open_contact_page(self):
        wd = self.app.wd
        # Open group page
        wd.find_element_by_xpath('//*[@id="nav"]/ul/li[1]/a').click()

    def create_contact(self, contact):
        wd = self.app.wd
        # Init contact creation
        wd.find_element_by_xpath('//*[@id="nav"]/ul/li[2]/a').click()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("quickadd").click()
        wd.find_element_by_name("submit").click()

    def delete_contact_by_number(self, number):
        wd = self.app.wd
        self.open_contact_page()
        checkboxess = wd.find_elements_by_name("selected[]")
        checkboxess[number].click()
        wd.find_element_by_xpath('//*[@id="content"]/form[2]/div[2]/input').click()

    def delete_all_contacts(self):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_xpath('//*[@id="MassCB"]').click()
        wd.find_element_by_xpath('//*[@id="content"]/form[2]/div[2]/input').click()

    def count_c(self):
        wd = self.app.wd
        self.open_contact_page()
        checkboxes = wd.find_elements_by_name("selected[]")
        return len(checkboxes)