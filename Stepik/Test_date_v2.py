import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

url = 'https://demoqa.com/date-picker'
driver.get(url)

"""Находим поле ввода даты и очищаем его"""

data_picker = driver.find_element(By.ID, 'datePickerMonthYearInput')
today = data_picker.get_attribute('value')
data_picker.send_keys(Keys.CONTROL + 'a')
data_picker.send_keys(Keys.DELETE)

"""Генерируем новую дату"""

next_day = int(today[3:5]) + 10
if next_day > 31:
    next_month = int(today[:2])+1
    next_day = next_day - 31
    next_year = today[6:]
    if next_month > 12:
        next_month = 1
        next_year += 1
else:
    next_month = today[:2]
    next_year = today[6:]

next_date = str(next_day) + '/' + str(next_month) + today[5:]
data_picker.send_keys(next_date)
print('Новая дата: ' + next_date)

time.sleep(5)
driver.quit()