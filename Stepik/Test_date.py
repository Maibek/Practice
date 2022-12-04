import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

url = 'https://demoqa.com/date-picker'

driver.get(url)