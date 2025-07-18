from pages.translate_page import TranslatePage
from confest import driver
from utils.cookie_avoider import bypass_google_consent


def test_text_validation(driver):
 page = TranslatePage(driver)
 page.open()
