import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    checkout_btn = 'checkout'


    # Getters
    def get_checkout_btn(self):
        return WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.ID, self.checkout_btn)))


    # Actions
    def click_checkout_btn(self):
        self.get_checkout_btn().click()
        print('Click "Checkout" button.')


    # Methods
    def confirm_product(self):
        self.get_current_url()

        self.click_checkout_btn()
        print('Click "Checkout" button.')
