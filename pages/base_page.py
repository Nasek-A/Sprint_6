import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    SCOOTER_LOGO = (
    By.XPATH,
    "//img[@alt='Scooter']/parent::a"
    )

    YANDEX_LOGO = (
    By.XPATH,
    "//img[@alt='Yandex']/parent::a"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    @allure.step("Открыть страницу: {url}")
    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Найти видимый элемент {locator}")
    def find_visible_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Найти элемент {locator} в DOM")
    def find_present_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Прокрутить страницу до элемента {locator}")
    def scroll_to_element(self, locator):
        element = self.find_present_element(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )

    @allure.step("Нажать на элемент {locator}")
    def click_element(self, locator):
        self.scroll_to_element(locator)
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Нажать на элемент {locator}, если он появился")
    def click_element_if_present(self, locator, timeout=2):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            ).click()
        except TimeoutException:
            pass

    @allure.step("Ввести текст «{text}» в поле {locator}")
    def type_text(self, locator, text):
        self.find_visible_element(locator).send_keys(text)

    @allure.step("Нажать клавишу в поле {locator}")
    def press_key(self, locator, key):
        self.find_visible_element(locator).send_keys(key)

    @allure.step("Получить текст элемента {locator}")
    def get_text(self, locator):
        return self.find_visible_element(locator).text

    @allure.step("Дождаться значения «{value}» у атрибута {attribute} элемента {locator}")
    def wait_for_attribute_value(self, locator, attribute, value):
        return self.wait.until(
            EC.text_to_be_present_in_element_attribute(
                locator, attribute, value
            )
        )

    @allure.step("Получить текущий адрес страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Дождаться адреса страницы: {url}")
    def wait_for_url(self, url):
        return self.wait.until(EC.url_to_be(url))

    @allure.step("Дождаться, что адрес страницы содержит «{part}»")
    def wait_for_url_contains(self, part):
        return self.wait.until(EC.url_contains(part))

    @allure.step("Переключиться на новое окно браузера")
    def switch_to_new_window(self, windows_before):
        self.wait.until(
            lambda driver: len(driver.window_handles) > len(windows_before)
        )
        new_window = next(
            window for window in self.driver.window_handles
            if window not in windows_before
        )
        self.driver.switch_to.window(new_window)

    @allure.step("Нажать на логотип Самоката")
    def click_scooter_logo(self):
        self.click_element(self.SCOOTER_LOGO)

    @allure.step("Нажать на логотип Яндекса и перейти в новое окно")
    def click_yandex_logo(self):
        windows_before = self.driver.window_handles
        self.click_element(self.YANDEX_LOGO)
        self.switch_to_new_window(windows_before)