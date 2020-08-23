from selenium import webdriver
import time
import unittest

from Pages.homePage import HomePage
from Pages.loginPage import LoginPage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("..\\drivers\\chromedriver.exe")
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()

    def test_login_valid(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        login= LoginPage(self.driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        home=HomePage(self.driver)
        home.click_welcome()
        home.click_logout()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__=='__main__':
    unittest.main()
