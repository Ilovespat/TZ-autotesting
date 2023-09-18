from PageObjects.PageObjects import Helper
from loguru import logger


# Два сценария в одном файле с использованием фикстуры и логированием в файл
def test_tensorru(browser):
    logger.info('# Запуск сценария 1.')
    tensor_page = Helper(browser)
    tensor_page.go_to_site()
    tensor_page.go_to_tensor_ru()

    logger.info('# Проверка перехода на сайт tensor.ru')
    assert "tensor.ru" in browser.current_url

    logger.info('# Ищем блок "Сила в людях"')
    assert tensor_page.where_is_power().is_displayed()

    logger.info('# Проверка перехода на страницу "Подробнее"')
    tensor_page.where_is_about()
    assert "about" in browser.current_url

    logger.info('# Проверка отображения блока "работаем"')
    assert tensor_page.where_is_work().is_displayed()

    logger.info('# Проверка размера изображений в блоке "работаем"')
    assert tensor_page.image_same_size()

    logger.info('# Завершение сценария 1')


def test_sbisru(browser):
    logger.info('# Запуск сценария 2"')

    sbis_page = Helper(browser)
    sbis_page.go_to_site()
    sbis_page.go_to_contacts()

    logger.info('# Проверка открытия сайта на нужном регионе')
    assert "г. Санкт-Петербург" in browser.title

    logger.info('# Проверка отображения блока с партнерами')
    assert sbis_page.where_is_partnersspb().is_displayed()

    logger.info('# Проверяем изменение региона и списка партнеров')
    assert sbis_page.go_to_kamchatka()
    assert "Камчатский край" in browser.title
    assert "kamchatskij-kraj" in browser.current_url

    logger.info('# Завершение сценария 2')


logger.add("LOG_TENSOR_{time}.log", level='INFO',
           format="<lvl>[</lvl><c>{time:DD.MM.YYYY HH:mm:ss.SSS}</c><lvl>]</lvl> <lvl>{message}</lvl>", catch='True')
