from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def bypass_google_consent(driver, timeout=5):

    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Accept all')]"))
        )
        driver.find_element(By.XPATH, "//button[contains(., 'Accept all')]").click()
    except:
        try:
            WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Decline all')]"))
            )
            driver.find_element(By.XPATH, "//button[contains(., 'Decline all')]").click()
        except:
            pass