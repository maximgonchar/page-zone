import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestLang:
    def test_choose_language(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        wait = WebDriverWait(browser, 5)
        browser.get(link)
        button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.btn-add-to-basket')))
        assert button != None