from Base import BasePage
from selenium.webdriver.common.by import By
import datetime


# Объекты, которые нужно найти на страницах, в переменных 
class Locators:
    LOCATOR_EL_CONTACTS = (By.LINK_TEXT, 'Контакты')
    LOCATOR_IMG_TENSOR = (By.CLASS_NAME, 'sbisru-Contacts__logo-tensor.mb-12')
    LOCATOR_EL_POWER = (By.XPATH, '//p [contains(text(),\'Сила в людях\')]')
    LOCATOR_EL_CLOSE_COOKIE = (By.XPATH, '//* [@id=\'container\']/div[3]/div[2]/div[2]')
    LOCATOR_EL_ABOUT = (By.XPATH, '//* [@id=\'container\']/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')
    LOCATOR_EL_WORK = (By.XPATH, '//h2 [contains(text(),\'Работаем\')]')
    LOCATORS_IMG_WORK = (By.CLASS_NAME, 'tensor_ru-About__block3-image')
    LOCATOR_EL_PARTNERS_SPB = (By.CLASS_NAME, "sbisru-Contacts-List__name.sbisru-Contacts-List--ellipsis.sbisru"
                                              "-Contacts__text--md.pb-4.pb-xm-12.pr-xm-32")
    LOCATOR_EL_REGION = (By.CLASS_NAME, "sbis_ru-Region-Chooser__text.sbis_ru-link")
    LOCATOR_EL_KAMCHATKA = (By.XPATH, '//span[contains(text(), \'Камчатский край\')]')
    LOCATOR_TITLE_KAMCHATKA = "Камчатский край"
    LOCATOR_EL_PARTNERS_KAMCHATKA = (By.CLASS_NAME, "sbisru-Contacts-List__name.sbisru-Contacts-List--ellipsis"
                                                    ".sbisru-Contacts__text--md.pb-4.pb-xm-12.pr-xm-32")
    # имя файла лога
    log_file_name = 'primer_autotesting_log{0}.txt'.format(str(datetime.datetime.today()))


# Ещё один wrapper для тестов
class Helper(BasePage):

    # переход в раздел контакты, находим лого, кликаем
    def go_to_tensor_ru(self):
        self.find_element(Locators.LOCATOR_EL_CONTACTS).click()
        self.find_element(Locators.LOCATOR_IMG_TENSOR).click()
        self.switch_window()
        return

    # поиск элемента 'Сила в людях' и остальных
    def where_is_power(self):
        return self.find_element(Locators.LOCATOR_EL_POWER)

    def where_is_about(self):
        self.find_element(Locators.LOCATOR_EL_CLOSE_COOKIE).click()  # для клика по нужному объекту закрываем ->
        # -> перекрывающее сообщение с куками
        self.find_element(Locators.LOCATOR_EL_ABOUT).click() # потом кликаем на нужный объект
        return

    def where_is_work(self):
        return self.find_element(Locators.LOCATOR_EL_WORK)

    # поиск и сравнение размеров картинок в разделе 'работаем'
    def image_same_size(self):
        image_list = self.find_elements(Locators.LOCATORS_IMG_WORK)
        width = set()
        height = set()
        for i in image_list:
            width.add(i.get_attribute("width"))
            height.add(i.get_attribute("height"))
        if len(width) == 1 and len(height) == 1:
            return True
        else:
            return False

    def go_to_contacts(self):
        self.find_element(Locators.LOCATOR_EL_CONTACTS).click()
        return

    def where_is_partnersspb(self):
        PARTNERS_SPB = self.find_element(Locators.LOCATOR_EL_PARTNERS_SPB)
        return PARTNERS_SPB

    # запоминаем блок с партнерами, меняем регион, проверяем изменился ли блок парнеров
    def go_to_kamchatka(self):
        PARTNERS_SPB = self.find_element(Locators.LOCATOR_EL_PARTNERS_SPB)
        self.find_element(Locators.LOCATOR_EL_REGION).click()
        self.find_element(Locators.LOCATOR_EL_KAMCHATKA).click()
        self.wait_element(Locators.LOCATOR_TITLE_KAMCHATKA)
        PARTNERS_KAMCHATKA = self.find_element(Locators.LOCATOR_EL_PARTNERS_KAMCHATKA)
        if PARTNERS_SPB != PARTNERS_KAMCHATKA:
            return True
        else:
            return False
