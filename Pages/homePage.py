class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_id = "welcome"
        self.logout_link_linkText = "Logout"
        self.login_button_id = "btnLogin"

    def click_welcome(self):
        self.driver.find_element_by_id("welcome").click()

    def click_logout(self):
        self.driver.find_element_by_link_text("Logout").click()
