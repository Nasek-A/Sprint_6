from pages.main_page import MainPage
from pages.order_page import OrderPage

from selenium.webdriver.support import expected_conditions as EC

class TestLogoNavigation:

    def test_scooter_logo_returns_to_main_page(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        
        main_page.click_order_button("top")
        order_page.click_scooter_logo()

        order_page.wait.until(
            EC.invisibility_of_element_located(
                order_page.NAME_INPUT
            )
        )

        assert driver.current_url == main_page.URL

 
    def test_yandex_logo_opens_dzen_in_new_tab(self, driver):
        main_page = MainPage(driver)

        main_page.open()

        windows_before = driver.window_handles

        main_page.click_yandex_logo()

        main_page.wait.until(
            lambda driver: len(driver.window_handles) > len(windows_before)
        )

        new_window = next(
            window for window in driver.window_handles
            if window not in windows_before
        )

        driver.switch_to.window(new_window)

        main_page.wait.until(
            lambda driver: "dzen.ru" in driver.current_url
        )

        assert "dzen.ru" in driver.current_url