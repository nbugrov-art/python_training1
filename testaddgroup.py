

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
        driver.get("http://localhost/addressbook/")
        driver.find_element(By.XPATH, "//input[@name='user']").click()
        driver.find_element(By.XPATH, "//input[@name='user']").clear()
        driver.find_element(By.XPATH, "//input[@name='user']").send_keys("admin")
        driver.find_element(By.XPATH, "//input[@name='pass']").click()
        driver.find_element(By.XPATH, "//input[@name='pass']").clear()
        driver.find_element(By.XPATH, "//input[@name='pass']").send_keys("secret")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()
        driver.find_element(By.LINK_TEXT, "add new").click()
        driver.find_element(By.NAME, "firstname").click()
        driver.find_element(By.NAME, "firstname").clear()
        driver.find_element(By.NAME, "firstname").send_keys("234234")
        driver.find_element(By.NAME, "submit").click()
        driver.find_element(By.LINK_TEXT, "Logout").click()
        driver.find_element(By.NAME, "user").clear()
        driver.find_element(By.NAME, "user").send_keys("admin")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()