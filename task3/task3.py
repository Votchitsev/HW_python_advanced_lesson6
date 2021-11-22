import selenium.webdriver.chrome.service
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import unittest
import time


class YandexPassportTest(unittest.TestCase):

    def setUp(self):

        path_to_chromedriver = os.path.abspath('chromedriver')
        ser = selenium.webdriver.chrome.service.Service(path_to_chromedriver)
        op = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=ser, options=op)

    def test_auth_to_yandex(self, user_login='insert your login', user_password='insert your password'):

        self.driver.get("https://passport.yandex.ru/auth")

        time.sleep(1)

        login = self.driver.find_element(By.ID, 'passp-field-login')
        login.send_keys(user_login)
        click_login = self.driver.find_element(By.ID, 'passp:sign-in')
        click_login.click()

        time.sleep(1)

        password = self.driver.find_element(By.ID, 'passp-field-passwd')
        password.send_keys(user_password)
        click_password = self.driver.find_element(By.ID, 'passp:sign-in')

        time.sleep(1)

        click_password.click()

        time.sleep(5)

        assert 'Яндекс ID' in self.driver.title

    def tearDown(self):
        self.driver.close()
