import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class GoogleTranslatePage(BasePage):
    URL = "https://translate.google.com/?hl=en&sl=os&tl=es&op=translate"

    SOURCE_TEXT_AREA = (By.XPATH, "//input[@placeholder='Search languages']")
    ORIGINAL_TEXT_AREA = (By.XPATH,"//textarea[@aria-label='Source text']")
    TRANSLATED_TEXT_AREA = (By.XPATH, "(//span[@lang='ru'])[1]")
    COOKIE_ACCEPT_BUTTON = (By.XPATH, "//button[contains(., 'Принять все') or contains(., 'Accept all')]")
    SWITCHER_SOURCE_LANG_BUTTON = (By.XPATH,"//*[@aria-label='More source languages']")
    SWITCHER_TARGET_LANG_BUTTON = (By.XPATH,"//*[@aria-label='More target languages']")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.URL)

    def select_source_language(self, language_name):
        self.click_element(self.SWITCHER_SOURCE_LANG_BUTTON)
        self.click_element(self.SOURCE_TEXT_AREA)
        self.send_keys(self.SOURCE_TEXT_AREA,language_name)
        chosen_language = self.find_element((By.XPATH, "//div[@class='vSUSRc']/div[@data-language-code='en']"))
        chosen_language.click()
        time.sleep(0.5)  # или использовать ожидание появления поля поиска


    def select_target_language(self, language_name):
        self.click_element(self.SWITCHER_TARGET_LANG_BUTTON)
        search_input = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH,"(//input[@aria-label='Search languages'])[2]")
        ))
        search_input.clear()
        search_input.send_keys(language_name)
        chosen_language = self.find_element((By.XPATH, "//div[@class='vSUSRc']/div[@data-language-code='ru']"))
        chosen_language.click()




    def enter_text_to_translate(self, text):
        """Вводит текст в поле для перевода."""
        self.send_keys(self.ORIGINAL_TEXT_AREA, text)

    def get_translated_text(self):
        """Получает переведенный текст."""
        return self.get_text(self.TRANSLATED_TEXT_AREA)


    def handle_cookie_consent(self):
        """
        Обрабатывает окно с согласием на файлы cookie, если оно появляется.
        """
        try:
            # Используем небольшой таймаут, чтобы дождаться появления кнопки
            self.wait.until(EC.element_to_be_clickable(self.COOKIE_ACCEPT_BUTTON))
            self.click_element(self.COOKIE_ACCEPT_BUTTON)
            print("Окно с согласием на файлы cookie закрыто.")
        except Exception:
            # Если кнопка не найдена в течение таймаута, это означает,
            # что окно не появилось. Это нормальная ситуация.
            print("Окно с согласием на файлы cookie не появилось или уже закрыто.")
            pass