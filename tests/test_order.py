import allure
import pytest

from selenium.webdriver.support import expected_conditions as EC

from data import ORDER_DATA
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Оформление заказа")
class TestOrder:
    @allure.title("Оформление заказа через кнопку {button_position}")
    @allure.story("Пользователь заполняет форму и подтверждает заказ")
    @pytest.mark.parametrize(
        "button_position, order_data",
        ORDER_DATA,
        ids=["top_button_ivan", "bottom_button_anna"]
    )

    def test_create_order(self, driver, button_position, order_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        # Открываем главную страницу и форму заказа
        main_page.open()
        main_page.click_order_button(button_position)
        order_page.wait.until(
            EC.visibility_of_element_located(order_page.NAME_INPUT)
        )

        # Заполняем обе части формы
        order_page.fill_order_form(order_data)

        # Отправляем и подтверждаем заказ
        order_page.click_order_button()
        order_page.confirm_order()

        # Проверяем успешное оформление заказа
        assert "Заказ оформлен" in order_page.get_success_message()