import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class OrderPage(BasePage):

    # Первая часть формы
    NAME_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Имя']"
    )

    SURNAME_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Фамилия']"
    )

    ADDRESS_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Адрес: куда привезти заказ']"
    )

    METRO_INPUT = (
        By.CSS_SELECTOR,
        "input.select-search__input"
    )

    PHONE_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Телефон: на него позвонит курьер']"
    )

    NEXT_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Далее']"
    )

    # Вторая часть формы
    DATE_INPUT = (
            By.XPATH,
            "//input[@placeholder='* Когда привезти самокат']"
    )
    
    RENT_PERIOD_DROPDOWN = (
            By.CSS_SELECTOR,
            "div.Dropdown-control"
    )
    
    BLACK_COLOR_CHECKBOX = (
            By.ID,
            "black"
    )
    
    GREY_COLOR_CHECKBOX = (
            By.ID,
            "grey"
    )

    COLOR_CHECKBOXES = {
        "black": BLACK_COLOR_CHECKBOX,
        "grey": GREY_COLOR_CHECKBOX,
    }
    
    COMMENT_INPUT = (
            By.XPATH,
            "//input[@placeholder='Комментарий для курьера']"
    )
    
    ORDER_BUTTON = (
            By.XPATH,
            "//div[contains(@class, 'Order_Buttons')]"
            "//button[normalize-space()='Заказать']"
    )
    
    CONFIRM_BUTTON = (
            By.XPATH,
            "//button[normalize-space()='Да']"
    )
    
    SUCCESS_MESSAGE = (
            By.CSS_SELECTOR,
            "div[class*='Order_ModalHeader']"
    )

    @allure.step("Ввести имя: {name}")
    def enter_name(self, name):
        self.type_text(self.NAME_INPUT, name)

    @allure.step("Ввести фамилию: {surname}")
    def enter_surname(self, surname):
        self.type_text(self.SURNAME_INPUT, surname)

    @allure.step("Ввести адрес доставки: {address}")
    def enter_address(self, address):
        self.type_text(self.ADDRESS_INPUT, address)
        
    @allure.step("Выбрать станцию метро: {metro}")
    def enter_metro(self, metro):
        self.click_element(self.METRO_INPUT)
        self.type_text(self.METRO_INPUT, metro)

        metro_option = (
            By.XPATH,
            f"//div[normalize-space()='{metro}']/parent::button"
        )
        self.click_element(metro_option)

    @allure.step("Ввести номер телефона: {phone}")
    def enter_phone(self, phone):
        self.type_text(self.PHONE_INPUT, phone)
    
    @allure.step("Перейти ко второй части формы заказа")
    def click_next_button(self):
        self.click_element(self.NEXT_BUTTON)

    @allure.step("Указать дату доставки: {date}")
    def enter_date(self, date):
        self.type_text(self.DATE_INPUT, date)
        self.press_key(self.DATE_INPUT, Keys.ESCAPE)

    @allure.step("Выбрать срок аренды: {period}")
    def select_rent_period(self, period):
        self.click_element(self.RENT_PERIOD_DROPDOWN)

        option = (
            By.XPATH,
            "//div[contains(@class, 'Dropdown-option') "
            f"and normalize-space()='{period}']"
        )
        self.click_element(option)

    @allure.step("Выбрать цвет самоката: {color}")    
    def select_color(self, color):
        if color not in self.COLOR_CHECKBOXES:
            raise ValueError(f"Неизвестный цвет самоката: {color}")
        self.click_element(self.COLOR_CHECKBOXES[color])

    @allure.step("Добавить комментарий курьеру")
    def enter_comment(self, comment):
        self.type_text(self.COMMENT_INPUT, comment)

    @allure.step("Заполнить данные клиента и адрес доставки")
    def fill_customer_details(self, data):
        self.enter_name(data["name"])
        self.enter_surname(data["surname"])
        self.enter_address(data["address"])
        self.enter_metro(data["metro"])
        self.enter_phone(data["phone"])

    @allure.step("Заполнить параметры аренды")
    def fill_rental_details(self, data):
        self.enter_date(data["date"])
        self.select_rent_period(data["period"])
        self.select_color(data["color"])
        self.enter_comment(data["comment"])

    @allure.step("Заполнить форму заказа целиком")
    def fill_order_form(self, data):
        self.fill_customer_details(data)
        self.click_next_button()
        self.fill_rental_details(data)

    @allure.step("Нажать кнопку «Заказать» в форме")
    def click_order_button(self):
        self.click_element(self.ORDER_BUTTON)

    @allure.step("Подтвердить оформление заказа")
    def confirm_order(self):
        self.click_element(self.CONFIRM_BUTTON)

    @allure.step("Получить сообщение об успешном оформлении заказа")
    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)      