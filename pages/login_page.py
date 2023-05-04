import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class LoginPage(Base):

    url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        super().__init__(driver)
        # self.driver = driver

    # Locators
    user_name = 'user-name'
    password = 'password'
    login_btn = 'login-button'
    compared_value = 'span.title' # Value from page "Products"

    # Getters
    def get_user_name(self):
        return WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.ID, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.ID, self.password)))

    def get_login_btn(self):
        return WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.ID, self.login_btn)))

    def get_compared_value(self):
        return WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.compared_value)))

    # Actions
    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print('Input user name')

    def input_password(self, password):
        self.get_password().send_keys(password)
        print('Input password')

    def click_login_button(self):
        self.get_login_btn().click()
        print('Click login button')

    # Methods
    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.input_user_name("standard_user")
        self.input_password("secret_sauce")

        self.click_login_button()

        self.assert_word(self.get_compared_value(), 'Products')
