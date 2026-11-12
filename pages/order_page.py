from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
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

    
    def enter_name(self, name):
        self.wait.until(
            EC.visibility_of_element_located(
                self.NAME_INPUT
            )
        ).send_keys(name)

    def enter_surname(self, surname):
        self.wait.until(
            EC.visibility_of_element_located(
                self.SURNAME_INPUT
            )
        ).send_keys(surname)

    def enter_address(self, address):
        self.wait.until(
            EC.visibility_of_element_located(
                self.ADDRESS_INPUT
            )
        ).send_keys(address)
        
      
    def enter_metro(self, metro):
        metro_input = self.wait.until(
            EC.element_to_be_clickable(self.METRO_INPUT)
    )
        metro_input.click()

        metro_option = (
            By.XPATH,
            f".//div[normalize-space()='{metro}']/parent::button"
    )

        self.wait.until(
            EC.element_to_be_clickable(metro_option)
        ).click()


    def enter_phone(self, phone):
        self.wait.until(
            EC.visibility_of_element_located(
                self.PHONE_INPUT
            )
        ).send_keys(phone)

    def click_next_button(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.NEXT_BUTTON
            )
        ).click()
    
    def enter_date(self, date):
        date_input = self.wait.until(
            EC.element_to_be_clickable(self.DATE_INPUT)
        )
        date_input.send_keys(date)
        date_input.send_keys(Keys.ESCAPE)

    def select_rent_period(self, period):
        self.wait.until(
            EC.element_to_be_clickable(
                self.RENT_PERIOD_DROPDOWN
            )
        ).click()

        option = (
            By.XPATH,
            f"//div[contains(@class, 'Dropdown-option') and normalize-space()='{period}']"
        )

        self.wait.until(
            EC.element_to_be_clickable(option)
        ).click()

        
    def select_color(self, color):
        if color == "black":
            locator = self.BLACK_COLOR_CHECKBOX
        elif color == "grey":
            locator = self.GREY_COLOR_CHECKBOX
        else:
            raise ValueError(f"Unknown color: {color}")

        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def fill_order_form(self, data):
        # Первая часть формы
        self.enter_name(data["name"])
        self.enter_surname(data["surname"])
        self.enter_address(data["address"])
        self.enter_metro(data["metro"])
        self.enter_phone(data["phone"])

        self.click_next_button()

        # Вторая часть формы
        self.enter_date(data["date"])
        self.select_rent_period(data["period"])
        self.select_color(data["color"])
        self.enter_comment(data["comment"])

    def enter_comment(self, comment):
        self.wait.until(
            EC.visibility_of_element_located(
                self.COMMENT_INPUT
            )
        ).send_keys(comment)

    def click_order_button(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.ORDER_BUTTON
            )
        ).click()

    def confirm_order(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.CONFIRM_BUTTON
            )
        ).click()

    def get_success_message(self):
        message = self.wait.until(
            EC.visibility_of_element_located(
                self.SUCCESS_MESSAGE
            )
        )
        return message.text         

   