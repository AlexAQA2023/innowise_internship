from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TranslatePage:
    def __init__(self,driver):
        self.driver = driver
        self.url = 'https://translate.google.com/?hl=en'

    def open(self):
        self.driver.get(self.url)

    def select_source_language(self):
        wait = WebDriverWait(self.driver, 10)

        source_option = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@data-tooltip-id="ucj-7-en-tooltip"]'))
        )
        source_option.click()


    def select_target_language(self):
        wait = WebDriverWait(self.driver, 10)
        target_option = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[data-tooltip-id="ucj-10-ru-tooltip"]'))
        )
        target_option.click()

    def expand_target_language(self):
        wait = WebDriverWait(self.driver, 10)
        target_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='More target languages']"))
        )
        target_button.click()

    def expand_source_language(self):
        wait = WebDriverWait(self.driver, 10)
        source_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='More source languages']"))
        )
        source_button.click()

    def enter_test_text(self,text):
        text_input = self.driver.find_element(By.XPATH, "//textarea[@aria-label='Source text']")
        text_input.clear()
        text_input.send_keys(text)

    def check_text(self,text):
        assert self.driver.find_element(By.XPATH, "//div[@aria-label='Translation results']").is_displayed()