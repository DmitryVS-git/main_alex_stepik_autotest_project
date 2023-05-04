import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    add_product_1_btn = 'add-to-cart-sauce-labs-backpack'
    add_product_2_btn = 'add-to-cart-sauce-labs-bike-light'
    add_product_3_btn = 'add-to-cart-sauce-labs-bolt-t-shirt'
    cart = 'shopping_cart_container'
    menu_btn = 'react-burger-menu-btn'
    link_about = 'about_sidebar_link'

    # Getters
    def get_select_product_1(self):
        return WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.ID, self.add_product_1_btn)))

    def get_select_product_2(self):
        return WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.ID, self.add_product_2_btn)))

    def get_select_product_3(self):
        return WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.ID, self.add_product_3_btn)))

    def get_cart(self):
        return WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.ID, self.cart)))

    def get_menu_btn(self):
        return WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.ID, self.menu_btn)))

    def get_link_about(self):
        return WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.ID, self.link_about)))


    # Actions
    def click_select_product_1(self):
        self.get_select_product_1().click()
        print('Click "Add to cart" button of product_1.')

    def click_select_product_2(self):
        self.get_select_product_2().click()
        print('Click "Add to cart" button of product_2.')

    def click_select_product_3(self):
        self.get_select_product_3().click()
        print('Click "Add to cart" button of product_3.')

    def click_cart(self):
        self.get_cart().click()
        print('Click cart. Entering.')

    def click_menu_btn(self):
        self.get_menu_btn().click()
        print('Click [burger menu] button.')

    def click_link_about(self):
        self.get_link_about().click()
        print('Click "about" link. Go to saucelabs.com')

    # Methods
    def select_product_1(self):
        self.get_current_url()

        self.click_select_product_1()
        self.click_cart()

    def select_product_2(self):
        self.get_current_url()

        self.click_select_product_2()
        self.click_cart()

    def select_product_3(self):
        self.get_current_url()

        self.click_select_product_3()
        self.click_cart()

    def select_menu_about(self):
        self.get_current_url()

        self.click_menu_btn()
        self.click_link_about()

        self.assert_url('https://saucelabs.com/')