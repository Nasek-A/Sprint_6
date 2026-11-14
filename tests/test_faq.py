import allure
import pytest

from data import FAQ_DATA
from pages.main_page import MainPage

@allure.feature("Раздел FAQ")   
class TestFaq:
    @allure.title("Проверка ответа на вопрос FAQ № {question_number}")
    @allure.story("Пользователь раскрывает вопрос и видит ответ")
    
    @pytest.mark.parametrize(
        "question_number, expected_answer",
        FAQ_DATA,
        ids=[f"question_{i}" for i in range(8)]
    )

    def test_faq_questions(
        self, driver, question_number, expected_answer
    ):
        main_page = MainPage(driver)

        main_page.open()
        main_page.scroll_to_faq()
        main_page.click_question(question_number)

        assert main_page.is_question_expanded(question_number)
        assert main_page.get_answer_text(question_number) == expected_answer