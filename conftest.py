import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Select language: ar, ru, en, ... ")

@pytest.fixture(scope="function")
def browser(request):
    site_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': site_language})
    print("\nStart browser Chrome fot test...")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nQuit browser..")
    browser.quit()
