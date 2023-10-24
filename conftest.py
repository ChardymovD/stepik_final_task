import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Select preferred language for tests')

@pytest.fixture(scope='function')
def language(request):
    return request.config.getoption('language')

@pytest.fixture(scope='function')
def browser(language):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
