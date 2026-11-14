import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


class MainPage(BasePage):

    URL = "https://qa-scooter.praktikum-services.ru/"

    # Кнопки заказа
    TOP_ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'Header_Nav')]//button[normalize-space()='Заказать']"
    )

    BOTTOM_ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'Home_FinishButton')]//button[normalize-space()='Заказать']"
    )

    # Заголовок раздела FAQ
    FAQ_TITLE = (
        By.XPATH,
        "//*[contains(text(), 'Вопросы о важном')]"
    )

    QUESTION = (
        By.ID,
        "accordion__heading-{}"
    )

    ANSWER = (
        By.ID,
        "accordion__panel-{}"
    )

    COOKIE_ACCEPT_BUTTON = (
        By.ID,
        "rcc-confirm-button"
    )
    @allure.step("Открыть главную страницу Самоката")
    def open(self):
        self.open_page(self.URL)
        self.accept_cookies()

    @allure.step("Закрыть уведомление о cookie, если оно отображается")
    def accept_cookies(self):
        try:
            WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable(self.COOKIE_ACCEPT_BUTTON)
            ).click()
        except TimeoutException:
                pass
        
    @allure.step("Прокрутить страницу до блока FAQ")
    def scroll_to_faq(self):
        faq = self.wait.until(
            EC.presence_of_element_located(
                self.FAQ_TITLE
            )
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView();", faq
        )

    def _get_question_locator(self, question_number):
        return (
            self.QUESTION[0],
            self.QUESTION[1].format(question_number)
        )


    def _get_answer_locator(self, question_number):
        return (
            self.ANSWER[0],
            self.ANSWER[1].format(question_number)
        )


    @allure.step("Открыть вопрос FAQ № {question_number}")
    def click_question(self, question_number):
        question = self.wait.until(
            EC.element_to_be_clickable(
                self._get_question_locator(question_number)
            )
        )
        question.click()


    @allure.step("Проверить, что вопрос FAQ № {question_number} раскрыт")
    def is_question_expanded(self, question_number):
        return self.wait.until(
            EC.text_to_be_present_in_element_attribute(
                self._get_question_locator(question_number),
                "aria-expanded",
                "true"
            )
        )


    @allure.step("Получить текст ответа на вопрос FAQ № {question_number}")
    def get_answer_text(self, question_number):
        answer = self.wait.until(
            EC.visibility_of_element_located(
                self._get_answer_locator(question_number)
            )
        )
        return answer.text


    @allure.step("Нажать кнопку заказа ({position})")
    def click_order_button(self, position):
        buttons = {
            "top": self.TOP_ORDER_BUTTON,
            "bottom": self.BOTTOM_ORDER_BUTTON
        }

        if position not in buttons:
            raise ValueError(
                f"Неизвестное расположение кнопки заказа: {position}"
        )

        self.wait.until(
            EC.element_to_be_clickable(buttons[position])
        )

        button = self.driver.find_element(*buttons[position])

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            button
        )

        self.wait.until(
            EC.element_to_be_clickable(buttons[position])
        ).click()