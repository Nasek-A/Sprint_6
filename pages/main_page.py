import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from urls import MAIN_PAGE_URL

class MainPage(BasePage):

    # Кнопки заказа
    TOP_ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'Header_Nav')]//button[normalize-space()='Заказать']"
    )

    BOTTOM_ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'Home_FinishButton')]//button[normalize-space()='Заказать']"
    )

    ORDER_BUTTONS = {
        "top": TOP_ORDER_BUTTON,
        "bottom": BOTTOM_ORDER_BUTTON,
    }

    # Заголовок раздела FAQ
    FAQ_TITLE = (
        By.XPATH,
        "//*[contains(text(), 'Вопросы о важном')]"
    )

    QUESTION_ID = "accordion__heading-{}"
    ANSWER_ID = "accordion__panel-{}"

    COOKIE_ACCEPT_BUTTON = (
        By.ID,
        "rcc-confirm-button"
    )

    @allure.step("Открыть главную страницу Самоката")
    def open(self):
        self.open_page(MAIN_PAGE_URL)
        self.accept_cookies()

    @allure.step("Закрыть уведомление о cookie, если оно отображается")
    def accept_cookies(self):
        self.click_element_if_present(self.COOKIE_ACCEPT_BUTTON)
        
    @allure.step("Прокрутить страницу до блока FAQ")
    def scroll_to_faq(self):
        self.scroll_to_element(self.FAQ_TITLE)

    @allure.step("Открыть вопрос FAQ № {question_number}")
    def click_question(self, question_number):
        locator = (By.ID, self.QUESTION_ID.format(question_number))
        self.click_element(locator)

    @allure.step("Проверить, что вопрос FAQ № {question_number} раскрыт")
    def is_question_expanded(self, question_number):
         locator = (By.ID, self.QUESTION_ID.format(question_number))
         return self.wait_for_attribute_value(locator, "aria-expanded", "true")

    @allure.step("Получить текст ответа на вопрос FAQ № {question_number}")
    def get_answer_text(self, question_number):
        locator = (By.ID, self.ANSWER_ID.format(question_number))
        return self.get_text(locator)

    @allure.step("Нажать кнопку заказа ({position})")
    def click_order_button(self, position):
        if position not in self.ORDER_BUTTONS:
            raise ValueError(
                f"Неизвестное расположение кнопки заказа: {position}"
            )
        self.click_element(self.ORDER_BUTTONS[position])

    @allure.step("Дождаться открытия главной страницы Самоката")
    def wait_for_main_page(self):
        return self.wait_for_url(MAIN_PAGE_URL)