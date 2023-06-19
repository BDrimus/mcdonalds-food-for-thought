import customtkinter as ctk

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from gui import display_gui

def fill_out_survey(entry_code, date_of_order, time_of_order, amount_spent):
    geckodriver_path = "/geckodriver"
    driver = webdriver.Firefox(service=Service(executable_path=geckodriver_path))
    driver.get("https://www.mcdfoodforthoughts.com")

    print(entry_code, date_of_order, time_of_order, amount_spent)

    # Enter the entry code
    # entry_code_field = driver.find_element_by_id("CN1")
    # entry_code_field.send_keys(entry_code)

    button_locator = (By.ID, "NextButton")
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(button_locator)
    )
    button.click()

    button_locator = (By.CSS_SELECTOR, "div.rbloption:nth-child(1) > span:nth-child(1) > label:nth-child(2)")
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(button_locator)
    )
    button.click()

    button_locator = (By.ID, "NextButton")
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(button_locator)
    )
    button.click()

entry_code, date_of_order, time_of_order, amount_spent = display_gui()

fill_out_survey(entry_code, date_of_order, time_of_order, amount_spent)