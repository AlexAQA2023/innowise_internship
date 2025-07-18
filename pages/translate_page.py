from selenium.webdriver.common.by import By


class TranslatePage:
    def __init__(self,driver):
        self.driver = driver
        self.url = 'https://translate.google.com/?hl=en'

    def open(self):
        self.driver.get(self.url)

    def select_language(self,source='English',target='Russian'):
        self.driver.find_element(By.XPATH, "//button[@aria-label='More source languages']").click()
        self.driver.find_element(By.XPATH, f"//div[text()='{source}']").click()
        self.driver.find_element(By.XPATH,"//button[@aria-label='More target languages']").click()
        self.driver.find_element(By.XPATH, f"//div[text()='{target}']").click()

    def enter_text(self,text):
        text_input = self.driver.find_element(By.XPATH, "//textarea[@aria-label='Source text']")
        text_input.clear()
        text_input.send_keys(text)

    def check_text(self,text):
        assert self.driver.find_element(By.XPATH, "//div[@aria-label='Translation results']").is_displayed()