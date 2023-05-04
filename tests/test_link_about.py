import time

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


def test_link_about():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(chrome_options=options)

    print('Start test')
    login = LoginPage(driver)
    login.authorization()

    main_page = MainPage(driver)
    main_page.select_menu_about()
    time.sleep(2)



