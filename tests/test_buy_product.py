import time

from pages.login_page import Login_page

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_buy_product():
    driver = webdriver.Chrome()

    login = Login_page(driver)
    login.authorization()

    enter_shopping_cart = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, 'shopping_cart_container')))
    enter_shopping_cart.click()

    time.sleep(2)
    print('Go to shopping cart')


