from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def fill_out_survey(entry_code, date_of_order, time_of_order, amount_spent):
    geckodriver_path = "/geckodriver"
    driver = webdriver.Firefox(service=Service(executable_path=geckodriver_path))
    driver.get("https://www.mcdfoodforthoughts.com")

    # Enter the entry code
    # entry_code_field = driver.find_element_by_id("CN1")
    # entry_code_field.send_keys(entry_code)

    button_locator = (By.ID, "NextButton")

    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(button_locator)
    )

    button.click()

fill_out_survey("12345678901234567890123456789012", "01/01/2021", "12:00", "10.00")