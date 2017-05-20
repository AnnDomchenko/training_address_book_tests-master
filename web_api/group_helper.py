from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of
from models.group import Group

class GroupHelper:
    def __init__(self, app):
        self.app=app

    def is_group_present(self):
        self.open_group_page()
        return self.app.is_element_present(By.NAME, "selected[]")

    def open_group_page(self):
        wd = self.app.wd
        # Open group page
        wd.find_element_by_xpath('//*[@id="nav"]/ul/li[3]/a').click()

    def create(self, group):
        wd = self.app.wd
        # Init group creation
        wd.find_element_by_name("new").click()
        # Fill group form
        if group.name is not None:
            wd.find_element_by_name("group_name").click()
            wd.find_element_by_name("group_name").clear()
            wd.find_element_by_name("group_name").send_keys(group.name)
        if group.header is not None:
            wd.find_element_by_name("group_header").click()
            wd.find_element_by_name("group_header").clear()
            wd.find_element_by_name("group_header").send_keys(group.header)
        if group.footer is not None:
            wd.find_element_by_name("group_footer").click()
            wd.find_element_by_name("group_footer").clear()
            wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Submit group
        wd.find_element_by_name("submit").click()

    def delete_by_number(self, number):
        wd = self.app.wd
        checkboxes = wd.find_elements_by_name("selected[]")
        checkboxes[number].click()
        wd.find_element_by_name("delete").click()

    def delete_groups(self):
        wd = self.app.wd
        wd.open_group_page()
        checkboxes=wd.find_elements_by_name("selected[]")
        while checkboxes != []:
            wd.find_elements_by_name("selected[]")
            wd.find_element_by_name("delete").click()

    def return_to_group_page(self):
        wd = self.app.wd
        # Return to group page
        wd.find_element_by_link_text("group page").click()

    def get_list(self):
        wd=self.app.wd
        self.open_group_page()
        checkboxes=wd.find_elements_by_name("selected[]")
        groups=[]
        for checkbox in checkboxes:
            name=checkbox.get_attribute("title")[8:-1]
            id=int(checkbox.get_attribute("value"))
            groups.append(Group(name=name,id=id))
        return groups

    # def modify_by_number(self, number, data_to_modify):
    #     data_to_modify.name
    #     data_to_modify.header
    #     data_to_modify.footer

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        checkboxes = wd.find_elements_by_name("selected[]")
        return len(checkboxes)

