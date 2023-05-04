import time

import pytest

from pages.cart_page import CartPage
from pages.client_information_page import ClientInformationPage
from pages.finish_page import FinishPage
from pages.login_page import LoginPage

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from pages.main_page import MainPage
from pages.payment_page import PaymentPage

# @pytest.mark.run(order=3)
def test_buy_product_1(set_group):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(chrome_options=options)

    print('Start test 1')
    login = LoginPage(driver)
    login.authorization()

    main_page = MainPage(driver)
    main_page.select_product_1()
    print('Go to shopping cart')

    cart_page = CartPage(driver)
    cart_page.confirm_product()
    print('Go to "Checkout your information" page')

    client_info_page = ClientInformationPage(driver)
    client_info_page.input_information()
    print('Go to "Checkout: Overview" page')

    payment_page = PaymentPage(driver)
    payment_page.payment()
    print('Make a payment and go to the finish page')

    finish_page = FinishPage(driver)
    finish_page.make_screenshot()
    print('Make a screenshot of the finish page')
    print('Finish test 1')

# @pytest.mark.run(order=1)
def test_buy_product_2():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(chrome_options=options)

    print('Start test 2')
    login = LoginPage(driver)
    login.authorization()

    main_page = MainPage(driver)
    main_page.select_product_2()
    print('Go to shopping cart')

    cart_page = CartPage(driver)
    cart_page.confirm_product()
    print('Go to "Checkout your information" page')

    print('Finish test 2')

# @pytest.mark.run(order=2)
def test_buy_product_3():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(chrome_options=options)

    print('Start test 3')
    login = LoginPage(driver)
    login.authorization()

    main_page = MainPage(driver)
    main_page.select_product_3()
    print('Go to shopping cart')

    cart_page = CartPage(driver)
    cart_page.confirm_product()
    print('Go to "Checkout your information" page')

    print('Finish test 3')




