from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import math
import random
import time

from config import geckodriver_path
from config import email

def generate_random_name():
    first_names = ('John', 'Andy', 'Joe')
    last_names = ('Johnson', 'Smith', 'Williams')

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    return first_name, last_name

def fill_out_survey(entry_code, date_of_order, time_of_order, amount_spent):

    def find_elements(driver, locator, timeout=10):
        try:
            return WebDriverWait(driver, timeout).until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            return []
        
    def click_until_id_not_present(driver, button_locator, target_id, timeout=10):
        while True:
            try:
                button_locator = (By.ID, "NextButton")
                button = WebDriverWait(driver, timeout).until(
                    EC.element_to_be_clickable(button_locator)
                )
                button.click()

                # Wait for the button to become stale (i.e., detached from the DOM)
                WebDriverWait(driver, timeout).until(
                    EC.staleness_of(button)
                )
            except TimeoutException:
                break

            found = False

            try:
                WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.ID, target_id))
                )
                found = True
            except TimeoutException:
                found = False

            if found:
                break
        
    def rate_all_5():
        # Count the number of rows in the table
        rows = driver.find_elements(By.XPATH, "//table/tbody/tr")
        num_rows = math.ceil(len(rows)//2)

        for i in range(1, num_rows + 1):
            button_locator_odd = (By.XPATH, f"//tr[contains(@class, 'InputRowOdd')][{i}]//input[@type='radio' and @value='5']")
            if i < 3:
                button_locator_even = (By.XPATH, f"//tr[contains(@class, 'InputRowEven')][{i}]//input[@type='radio' and @value='5']")

            buttons_odd = find_elements(driver, button_locator_odd)
            buttons_even = find_elements(driver, button_locator_even)

            for button in buttons_odd:
                driver.execute_script("arguments[0].checked = true;", button)

            for button in buttons_even:
                driver.execute_script("arguments[0].checked = true;", button)
    
    driver = webdriver.Firefox(service=Service(executable_path=geckodriver_path))
    driver.get("https://www.mcdfoodforthoughts.com")

    print(entry_code, date_of_order, time_of_order, amount_spent)

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

    field_locator = (By.ID, "CN1")
    field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(field_locator)
    )
    field.send_keys(entry_code.split("-")[0])

    field_locator = (By.ID, "CN2")
    field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(field_locator)
    )
    field.send_keys(entry_code.split("-")[1])

    field_locator = (By.ID, "CN3")
    field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(field_locator)
    )
    field.send_keys(entry_code.split("-")[2])

    field_locator = (By.ID, "AmountSpent1")
    field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(field_locator)
    )
    field.send_keys(amount_spent.split(".")[0])

    field_locator = (By.ID, "AmountSpent2")
    field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(field_locator)
    )
    field.send_keys(amount_spent.split(".")[1])

    button_locator = (By.ID, "NextButton")
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(button_locator)
    )
    button.click()

    button_locator = (By.ID, "textR000005.3")
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(button_locator)
    )
    button.click()

    button_locator = (By.ID, "NextButton")
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(button_locator)
    )
    button.click()

    for i in range(1, 18):
        button_locator = (By.ID, "NextButton")
        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(button_locator)
        )
        button.click()

    button_locator = (By.ID, "NextButton")
    target_id = "R000383.1"

    click_until_id_not_present(driver, button_locator, target_id)

    button_locator = (By.ID, "R000383.1")
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(button_locator)
    )
    driver.execute_script("arguments[0].click();", button)

    button_locator = (By.ID, "NextButton")
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(button_locator)
    )
    button.click()

    first_name, last_name = generate_random_name()

    field_locator = (By.ID, "S000068")
    field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(field_locator)
    )
    field.send_keys(first_name)

    field_locator = (By.ID, "S000073")
    field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(field_locator)
    )
    field.send_keys(last_name)

    field_locator = (By.ID, "S000070")
    field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(field_locator)
    )
    field.send_keys(email)

    field_locator = (By.ID, "S000071")
    field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(field_locator)
    )
    field.send_keys(email)

    button_locator = (By.ID, "NextButton")
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(button_locator)
    )
    button.click()