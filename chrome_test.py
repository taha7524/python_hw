from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Автоматически скачает нужную версию
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Открываем сайт для проверки
driver.get("https://www.google.com")
print("Страница открыта!")
print(f"Заголовок: {driver.title}")

# Ждем 3 секунды чтобы увидеть результат
import time
time.sleep(3)

# Закрываем браузер
driver.quit()
print("Браузер закрыт.")