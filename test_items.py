import pytest
from selenium.webdriver.common.by import By

def test_presence_button_add_card(browser):
    try:
        browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
        present_btn = True
    except:
        present_btn = False
    assert present_btn, 'No "ADD to CARD" button on page'