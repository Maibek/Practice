import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

"""Переменные"""

url = 'https://www.saucedemo.com/'
login_data = 'standard_user'
password_data = 'secret_sauce'

print('Приветствуем Вас в нашем магазине.')

driver.get(url)

login = driver.find_element(By.ID, 'user-name')
login.send_keys(login_data)

password = driver.find_element(By.ID, 'password')
password.send_keys(password_data)

login_btn = driver.find_element(By.NAME, 'login-button')
login_btn.click()
time.sleep(2)

print('Ознакомьтесь с каталогом товаров ниже:')


class Product:
    """Создание класса продуктов"""

    def __init__(self, num, name_product, price_product):
        self.num = num
        self.name_product = name_product
        self.price_product = price_product

    def catalog_product(self):
        """Вывод каталога товаров"""

        catalog = str(self.num) + ' ' + self.name_product + ' ' + self.price_product
        print(catalog)


"""Добавление объектов в класс"""

product_name = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
product_price = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
product_1 = Product(1, product_name.text, product_price.text)
product_1.catalog_product()

product_name = driver.find_element(By.XPATH, '//*[@id="item_0_title_link"]/div')
product_price = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[2]/div[2]/div[2]/div')
product_2 = Product(2, product_name.text, product_price.text)
product_2.catalog_product()

product_name = driver.find_element(By.XPATH, '//*[@id="item_1_title_link"]/div')
product_price = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[3]/div[2]/div[2]/div')
product_3 = Product(3, product_name.text, product_price.text)
product_3.catalog_product()

product_name = driver.find_element(By.XPATH, '//*[@id="item_5_title_link"]/div')
product_price = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[4]/div[2]/div[2]/div')
product_4 = Product(4, product_name.text, product_price.text)
product_4.catalog_product()

product_name = driver.find_element(By.XPATH, '//*[@id="item_2_title_link"]/div')
product_price = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[5]/div[2]/div[2]/div')
product_5 = Product(5, product_name.text, product_price.text)
product_5.catalog_product()

product_name = driver.find_element(By.XPATH, '//*[@id="item_3_title_link"]/div')
product_price = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[6]/div[2]/div[2]/div')
product_6 = Product(6, product_name.text, product_price.text)
product_6.catalog_product()

lst_product = [product_1, product_2, product_3, product_4, product_5, product_6]
lst_product_name = []

total_price = 0


def val():
    """Добавление товара в корзину"""
    product_selection = input('Введите номер товара, который желаете приобрести: ')
    global total_price
    total_price = 0
    num_of_product = 1
    while product_selection != 'NO':
        try:
            if 0 < int(product_selection) < 7:
                for i in lst_product:
                    if int(product_selection) == i.num:
                        lst_product_name.append(i.name_product)
                        total_price += float(i.price_product[1:])

                print('Вы выбрали ' + ''.join(lst_product_name[(num_of_product - 1):]))
                print('Количество товаров добавленное в корзину: ' + str(num_of_product))
                print('Общая цена товаров в корзине: ' + '$' + str(total_price))
                c = ''.join(lst_product_name[(num_of_product - 1):]).replace(' ', '-').lower()
                product_cart_btn = '//*[@id="add-to-cart-' + c + '"]'
                product_cart = driver.find_element(By.XPATH, product_cart_btn)
                product_cart.click()
                num_of_product += 1
            else:
                print('Введеный номер не соответствует ни одному товару.')
        except ValueError:
            print('Введеный номер не соответствует ни одному товару.')

        product_selection = input(
            'Введите номер товара, который желаете приобрести. Если вы выбрали все товары введите "NO": ').upper()


val()

"""Проверка колличества добавленных товаров в корзине"""

cart = driver.find_element(By.ID, 'shopping_cart_container')
cart.click()
time.sleep(2)

all_product = len(driver.find_elements(By.CLASS_NAME, 'inventory_item_name'))
if all_product == len(lst_product_name):
    print('Товаров в корзине: ' + str(len(lst_product_name)))
    print('Итого к оплате ' + '$' + str(total_price))
else:
    print('Количество товаров в корзине не соответствует добавленному количеству товаров пользователем.')

"""Заполнение данных покупателя"""

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

"""Проверка названия товаров в заказе"""

for i in range(all_product):
    value_product_name = driver.find_element(By.LINK_TEXT, ''.join(lst_product_name[i:i + 1]))
    assert value_product_name.text == ''.join(lst_product_name[i:i + 1])

"""Проверка суммы заказа"""

value_product_price = driver.find_element(By.XPATH, '//div[@class="summary_subtotal_label"]')
value_product_price_text = value_product_price.text.lstrip('Item total: $')
assert float(total_price) == float(value_product_price_text)

finish_btn = driver.find_element(By.ID, 'finish')
finish_btn.click()
time.sleep(5)
print('Заказ оформлен')

driver.quit()