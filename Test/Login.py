from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("..\\drivers\\chromedriver.exe")
# driver=webdriver.firefox()
# driver=webdriver.ie()

driver.set_page_load_timeout(30)

driver.get("https://www.amazon.in/")
driver.maximize_window()
time.sleep(30)
driver.quit()
