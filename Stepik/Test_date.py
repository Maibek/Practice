# Решил задачу 2-мя способами. Второй без библиотеки datatime, отправил вам на почту.
# Намерено сделал проверку по длительности месяца только равным 31 дню,
# для проверки количества дней в каждом месяце получится большая конструкция из функций if
# либо я плохо искал информацию в интернете.

import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

url = 'https://demoqa.com/date-picker'
driver.get(url)

"""Находим поле ввода даты и очищаем его"""

data_picker = driver.find_element(By.ID, 'datePickerMonthYearInput')
data_picker.send_keys(Keys.CONTROL + 'a')
data_picker.send_keys(Keys.DELETE)

"""Генерируем новую дату"""

date = datetime.now()
now_day = date.day
next_day = now_day + 10
if next_day > 31:
    next_day -= 31
    next_month = date.month + 1
    next_year = date.year
    if next_month > 12:
        next_month = 1
        next_year += 1
else:
    next_month = date.month
    next_year = date.year

next_date = str(next_month) + '/' + str(next_day) + '/' + str(next_year)
data_picker.send_keys(next_date)
print('Новая дата: ' + next_date)

time.sleep(5)
driver.quit()