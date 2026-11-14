import allure
from selenium.webdriver.support import expected_conditions as EC

from pages.main_page import MainPage
from pages.order_page import OrderPage

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

        main_page.wait.until(
        EC.url_to_be(main_page.URL)
        )

        assert driver.current_url == main_page.URL

    @allure.title("Клик по логотипу Яндекса открывает Дзен в новой вкладке")
    @allure.story("Переход на внешний сервис по логотипу Яндекса")
    def test_yandex_logo_opens_dzen_in_new_tab(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        windows_before = driver.window_handles
        main_page.click_yandex_logo()
        main_page.wait.until(
            lambda driver: len(driver.window_handles) > len(windows_before)
        )

        new_window = next(
            window 
            for window in driver.window_handles
            if window not in windows_before
        )

        driver.switch_to.window(new_window)
        main_page.wait.until(
            lambda driver: "dzen.ru" in driver.current_url
        )

        assert "dzen.ru" in driver.current_url