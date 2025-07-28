import pytest
from pages.google_translate_page import GoogleTranslatePage
from selenium.webdriver.remote.webdriver import WebDriver
class TestGoogleTranslate:

    def test_translation_and_ui_validation(self, driver: WebDriver):

        translate_page = GoogleTranslatePage(driver)
        translate_page.handle_cookie_consent()
        translate_page.select_source_language("English")
        translate_page.select_target_language("Russian")
        translate_page.enter_text_to_translate("Test")

        expected_translation = "Тест"
        actual_translation = translate_page.get_translated_text()

        print(f"Ожидаемый перевод: '{expected_translation}'")
        print(f"Полученный перевод: '{actual_translation}'")

        assert actual_translation == expected_translation, (
            f"Неверный перевод. Ожидалось: '{expected_translation}', "
            f"но получено: '{actual_translation}'."
        )
