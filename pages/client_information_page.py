import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class ClientInformationPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    first_name_input = 'first-name'
    last_name_input = 'last-name'
    zip_code_input = 'postal-code'
    continue_btn = 'continue'


    # Getters
    def get_first_name_input(self):
        return WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.ID, self.first_name_input)))

    def get_last_name_input(self):
        return WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.ID, self.last_name_input)))

    def get_zip_code_input(self):
        return WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.ID, self.zip_code_input)))

    def get_continue_btn(self):
        return WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.ID, self.continue_btn)))


    # Actions
    def fill_first_name_input(self, first_name):
        self.get_first_name_input().send_keys(first_name)
        print('Fill "First name" input.')

    def fill_last_name_input(self, last_name):
        self.get_last_name_input().send_keys(last_name)
        print('Fill "Last name" input.')

    def fill_zip_code_input(self, zip_code):
        self.get_zip_code_input().send_keys(zip_code)
        print('Fill "Zip_code" input.')


    def click_continue_btn(self):
        self.get_continue_btn().click()
        print('Click "Continue" button.')


    # Methods
    def input_information(self):
        self.get_current_url()

        self.fill_first_name_input('Dmitry')
        self.fill_last_name_input('Smirnov')
        self.fill_zip_code_input('1416')

        self.click_continue_btn()
