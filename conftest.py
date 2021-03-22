import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="сhrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Select language: ar, ru, en, ... ")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    site_language = request.config.getoption("language")
    if browser_name == "сhrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': site_language})
        print("\nStart browser Chrome fot test...")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", site_language)
        print("\nStart browser Firefox fot test...")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        print(f"\nUnknow browser " + browser_name + " is choose. Please, select Chrome or Firefox ")
    yield browser
    print("\nQuit browser..")
    browser.quit()

