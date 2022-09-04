import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
url = 'https://practice.automationtesting.in/'
driver.get(url)

shop_btn = driver.find_element(By.CSS_SELECTOR, '#menu-item-40 > a')
shop_btn.click()

main_menu = driver.find_element(By.ID, 'site-logo')
main_menu.click()

arrivals = len(driver.find_elements(By.CLASS_NAME, 'products'))
if arrivals == 3:
    print('Ok')
else:
    print('Error')

book = driver.find_element(By.CSS_SELECTOR, '#text-22-sub_row_1-0-2-0-0 > div > ul > li > a.woocommerce-LoopProduct-link > img')
book.click()

basket = driver.find_element(By.CSS_SELECTOR, '#product-160 > div.summary.entry-summary > form > button')
basket.click()

items_price = driver.find_element(By.CLASS_NAME, 'amount')
items_price_text = items_price.text
book_price = driver.find_element(By.CSS_SELECTOR, '#product-160 > div.summary.entry-summary > div:nth-child(2) > p > span')
book_price_text = book_price.text
assert items_price_text == book_price_text

time.sleep(2)
driver.quit()