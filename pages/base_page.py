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

    def open_page(self, url):
        self.driver.get(url)

    def click_scooter_logo(self):
        self.wait.until(
            EC.element_to_be_clickable(self.SCOOTER_LOGO)
        ).click()

    def click_yandex_logo(self):
        self.wait.until(
            EC.element_to_be_clickable(self.YANDEX_LOGO)
        ).click()