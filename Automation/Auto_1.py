from selenium import webdriver

driver = webdriver.chrome()
driver.maximize_window()
url = 'https://practice.automationtesting.in/'
driver.get(url)
