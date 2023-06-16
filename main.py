from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def fill_out_survey(entry_code, date_of_order, time_of_order, amount_spent):
    driver = webdriver.Firefox()