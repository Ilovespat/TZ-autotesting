import pytest
from selenium import webdriver

# Фикстура, инициализация webdriver и закрытие браузера после теста
@pytest.fixture
def browser(): #  фикстурная функция pytest
    browser = webdriver.Chrome() # Все вызовы WebDriver будут выполняться через объект драйвера
    browser.implicitly_wait(10) # неявное ожидание до появления элемента
    yield browser # ф-я генератор, конструкция разделяет ф-ю на до и поле тестов
    browser.close() # завершение сессии и закрытие браузера

