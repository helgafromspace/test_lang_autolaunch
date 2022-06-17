import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_button_add_to_basket_should_be_on_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket").is_enabled()
    assert button, 'button is missing'
    
