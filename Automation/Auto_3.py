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

book = driver.find_element(By.CSS_SELECTOR, '#text-22-sub_row_1-0-2-0-0 > div > ul > li > a.woocommerce-LoopProduct-link > img')
book.click()

description = driver.find_element(By.CSS_SELECTOR, '#product-160 > div.woocommerce-tabs.wc-tabs-wrapper > ul > li.description_tab.active > a')
description.click()

text = driver.find_element(By.ID, 'tab-description')
text_1 = text.text
assert 'Product Description' in text_1

time.sleep(2)
driver.quit()