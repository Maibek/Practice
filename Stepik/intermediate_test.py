import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

"""Переменные"""
url = 'https://www.saucedemo.com/'
login_data = 'standard_user'
password_data = 'secret_sauce'

driver.get(url)

print('Авторизация на сайте.')
"""Ввод данных логина"""

login = driver.find_element(By.ID, 'user-name')
login.send_keys(login_data)

"""Ввод данных пароля"""

password = driver.find_element(By.ID, 'password')
password.send_keys(password_data)

"""Нажатие на кнопку логина"""

login_btn = driver.find_element(By.NAME, 'login-button')
login_btn.click()

driver.execute_script("window.scrollBy(0, 100);")

print('Добавление товаров в корзину.')
"""Добавление товаров в корзину"""

product_1 = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
product_1.click()
product_name_1 = driver.find_element(By.XPATH, '//*[@id="item_1_title_link"]/div')
product_name_1_text = product_name_1.text
product_price_1 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[3]/div[2]/div[2]/div')
product_price_1_text = product_price_1.text.lstrip('$')


product_2 = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')
product_2.click()
product_name_2 = driver.find_element(By.XPATH, '//*[@id="item_5_title_link"]/div')
product_name_2_text = product_name_2.text
product_price_2 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[4]/div[2]/div[2]/div')
product_price_2_text = product_price_2.text.lstrip('$')

cart = driver.find_element(By.ID, 'shopping_cart_container')
cart.click()

print('Проверка количества товаров в корзине.')
"""Проверка количества товаров в корзине"""

all_product = len(driver.find_elements(By.CLASS_NAME, 'inventory_item_name'))
if all_product == 2:
    print('В корзине 2 товара.')
else:
    print('Количество товаров в корзине не соответствует 2.')

print('Оформление заказа.')
"""Оформление заказа"""

checkout = driver.find_element(By.NAME, 'checkout')
checkout.click()

first_name = driver.find_element(By.ID, 'first-name')
first_name.send_keys('First Name')

last_name = driver.find_element(By.ID, 'last-name')
last_name.send_keys('Last Name')

postal_code = driver.find_element(By.ID, 'postal-code')
postal_code.send_keys('Postal Code')

continue_btn = driver.find_element(By.NAME, 'continue')
continue_btn.click()

print('Проверка названия товаров в заказе.')
"""Проверка названия товаров в заказе"""

value_product_name_1 = driver.find_element(By.XPATH, '//*[@id="item_1_title_link"]/div')
value_product_name_1_text = value_product_name_1.text
assert value_product_name_1_text == product_name_1_text

value_product_name_2 = driver.find_element(By.XPATH, '//*[@id="item_5_title_link"]/div')
value_product_name_2_text = value_product_name_2.text
assert value_product_name_2_text == product_name_2_text

print('Проверка суммы заказа.')
"""Проверка суммы заказа"""

value_product_price = driver.find_element(By.XPATH, '//div[@class="summary_subtotal_label"]')
value_product_price_text = value_product_price.text.lstrip('Item total: $')
assert float(product_price_1_text) + float(product_price_2_text) == float(value_product_price_text)

finish_btn = driver.find_element(By.ID, 'finish')
finish_btn.click()
time.sleep(5)

print('Test ok')

driver.quit()