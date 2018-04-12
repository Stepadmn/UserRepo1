from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest


class LoginTests(unittest.TestCase):

    def test_validlogin(self):
        baseURL = "https://letskodeit.teachable.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseURL)

        lp = LoginPage(driver)
        lp.login("test@email.com","abcabc")

        verify = driver.find_element(By.XPATH,"//div[@id='navbar']//span[text()='User Settings']")
        if verify is not None:
            print("Login Successful")
        else:
            print("Login Failure")

        driver.close()

    def test_invalidlogin(self):
         baseURL = "https://letskodeit.teachable.com/"
         driver = webdriver.Firefox()
         driver.maximize_window()
         driver.implicitly_wait(5)
         driver.get(baseURL)

         lp = LoginPage(driver)
         lp.login("test@emailcom", "abcabc")

         verify = driver.find_element(By.XPATH, "//div[@id='navbar']//span[text()='User Settings']")
         if verify is not None:
            print("Login Successful")
         else:
            print("Login Failure")

         driver.close()