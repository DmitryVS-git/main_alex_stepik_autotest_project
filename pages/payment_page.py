import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class PaymentPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    finish_btn = 'finish'


    # Getters
    def get_finish_btn(self):
        return WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.ID, self.finish_btn)))


    # Actions
    def click_finish_btn(self):
        self.get_finish_btn().click()
        print('Click "Finish" button.')


    # Methods
    def payment(self):
        self.get_current_url()

        self.click_finish_btn()
