from pages.translate_page import TranslatePage


def test_text_validation(driver):
 page = TranslatePage(driver)
 page.open()
 page.select_language('English',"Russian")
 page.enter_text('King')
 page.check_text('King')