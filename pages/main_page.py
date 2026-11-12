from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

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

    def open(self):
        self.open_page(self.URL)
        self.accept_cookies()

    def scroll_to_faq(self):
        faq = self.wait.until(
            EC.presence_of_element_located(
                self.FAQ_TITLE
            )
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView();", faq
        )

    def click_question(self, question_number):
        locator = (
            self.QUESTION[0],
            self.QUESTION[1].format(question_number)
        )

        question = self.wait.until(
        EC.element_to_be_clickable(locator)
        )
        question.click()


    def is_question_expanded(self, question_number):
        locator = (
            self.QUESTION[0],
            self.QUESTION[1].format(question_number)
        )

        question = self.driver.find_element(*locator)

        return question.get_attribute("aria-expanded") == "true"


    def get_answer_text(self, question_number):
        locator = (
            self.ANSWER[0],
            self.ANSWER[1].format(question_number)
        )

        answer = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        return answer.text    

    def accept_cookies(self):
        try:
            self.wait.until(
                EC.element_to_be_clickable(self.COOKIE_ACCEPT_BUTTON)
            ).click()
        except TimeoutException:
            pass

    def click_order_button(self, position):
        if position == "top":
            locator = self.TOP_ORDER_BUTTON
        elif position == "bottom":
            locator = self.BOTTOM_ORDER_BUTTON
        else:
            raise ValueError(f"Unknown order button position: {position}")

        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()
