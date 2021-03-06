class SessionHelper:
    def __init__(self,app):
        self.app=app

    def login(self, username, password):
        self.app.open_home_page()
        wd = self.app.wd
        # Login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def logout(self):
        wd = self.app.wd
        # Logout
        wd.find_element_by_css_selector('form[name="logout"] > a').click()