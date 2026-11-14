import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage
from urls import DZEN_URL_PART, MAIN_PAGE_URL


@allure.feature("Навигация по логотипам")
class TestLogoNavigation:

    @allure.title("Клик по логотипу Самоката возвращает на главную страницу")
    @allure.story("Переход на главную страницу по логотипу сервиса")
    def test_scooter_logo_returns_to_main_page(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        main_page.click_order_button("top")
        order_page.click_scooter_logo()
        main_page.wait_for_main_page()

        assert driver.current_url == MAIN_PAGE_URL

    @allure.title("Клик по логотипу Яндекса открывает Дзен в новой вкладке")
    @allure.story("Переход на внешний сервис по логотипу Яндекса")
    def test_yandex_logo_opens_dzen_in_new_tab(self, driver):
        main_page = MainPage(driver)
        
        main_page.open()
        main_page.click_yandex_logo()
        main_page.wait_for_url_contains(DZEN_URL_PART)

        assert DZEN_URL_PART in main_page.get_current_url()