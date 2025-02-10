

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app_dynamics_job(self):
        driver = self.driver
        self.open_homepage(driver)
        self.login(driver)
        self.open_new_contact_page(driver)
        self.fill_contact_form(driver)
        self.submit_new_contact(driver)
        self.logout(driver)

    def logout(self, driver):
        # logout
        driver.find_element(By.LINK_TEXT, "Logout").click()

    def submit_new_contact(self, driver):
        # submit new contact
        driver.find_element(By.NAME, "submit").click()

    def fill_contact_form(self, driver):
        # fill contact firm
        driver.find_element(By.NAME, "firstname").click()
        driver.find_element(By.NAME, "firstname").clear()
        driver.find_element(By.NAME, "firstname").send_keys("234234")

    def open_new_contact_page(self, driver):
        # open add contact page
        driver.find_element(By.LINK_TEXT, "add new").click()

    def login(self, driver):
        # login
        driver.find_element(By.XPATH, "//input[@name='user']").click()
        driver.find_element(By.XPATH, "//input[@name='user']").clear()
        driver.find_element(By.XPATH, "//input[@name='user']").send_keys("admin")
        driver.find_element(By.XPATH, "//input[@name='pass']").click()
        driver.find_element(By.XPATH, "//input[@name='pass']").clear()
        driver.find_element(By.XPATH, "//input[@name='pass']").send_keys("secret")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()

    def open_homepage(self, driver):
        # Open home page
        driver.get("http://localhost/addressbook/")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()