from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.get("https://ya.ru")

href = driver.find_element(By.CSS_SELECTOR, '[data-statlog="2informers.stocks.item.1"]').get_attribute("href")

print(href)
driver.quit() #закрываем драйвер