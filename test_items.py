import pytest
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_presence_button_add_card(browser):
    browser.get(link)
    try:
        browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
        present_btn = True
    except:
        present_btn = False
    assert present_btn, 'No "ADD to CARD" button on page'