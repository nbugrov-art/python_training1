import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from group import Group

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.base_url = "http://localhost/addressbook/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app_dynamics_job(self):
        driver = self.driver
        self.open_homepage(driver)
        self.login(driver, "admin", "secret")
        self.open_new_contact_page(driver)
        self.fill_contact_form(driver, Group(name="12134"))
        self.submit_new_contact(driver)
        self.logout(driver)

    def test_2app_dynamics_job(self):
        driver = self.driver
        self.open_homepage(driver)
        self.login(driver, "admin", "secret")
        self.open_new_contact_page(driver)
        self.fill_contact_form(driver, Group(name=""))
        self.submit_new_contact(driver)
        self.logout(driver)

    def logout(self, driver):
        # logout
        driver.find_element(By.LINK_TEXT, "Logout").click()

    def submit_new_contact(self, driver):
        # submit new contact
        driver.find_element(By.NAME, "submit").click()

    def fill_contact_form(self, driver, group):
        # fill contact form
        driver.find_element(By.NAME, "firstname").click()
        driver.find_element(By.NAME, "firstname").clear()
        driver.find_element(By.NAME, "firstname").send_keys(group.name)

    def open_new_contact_page(self, driver):
        # open add contact page
        driver.find_element(By.LINK_TEXT, "add new").click()

    def login(self, driver, username, password):
        # login
        driver.find_element(By.XPATH, "//input[@name='user']").click()
        driver.find_element(By.XPATH, "//input[@name='user']").clear()
        driver.find_element(By.XPATH, "//input[@name='user']").send_keys(username)
        driver.find_element(By.XPATH, "//input[@name='pass']").click()
        driver.find_element(By.XPATH, "//input[@name='pass']").clear()
        driver.find_element(By.XPATH, "//input[@name='pass']").send_keys(password)
        driver.find_element(By.XPATH, "//input[@type='submit']").click()

    def open_homepage(self, driver):
        # Open home page
        driver.get(self.base_url)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()