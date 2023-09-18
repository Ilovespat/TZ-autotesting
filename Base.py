from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Базовые методы для работы с WebDriver и обертка для WebDriverWait
class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.base_url = 'https://sbis.ru/'

    def find_element(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Не найден элемент по локатору {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Не найден элемент по локатору {locator}")

    def wait_element(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.title_contains(locator),
                                                       message=f"Долгое ожидание обновления страницы")

    def switch_window(self):
        return self.browser.switch_to.window(self.browser.window_handles[1])

    def go_to_site(self):
        return self.browser.get(self.base_url)
