import pytest
from selenium import webdriver

# Фикстура, инициализация webdriver и закрытие браузера после теста 
@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.close()

