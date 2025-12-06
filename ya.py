#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager
#from time import sleep

#browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#browser. maximize_window()
#browser.get("https://ya.ru/")
##browser.save_screenshot("./ya.png")
#browser.quit()


#from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

#driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

#driver. maximize_window()
#driver.get("https://ya.ru/")
#driver.save_screenshot("./ya.png")
#driver.quit()


from time import sleep
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
ff = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

def make_screenshot(browser):
	browser.maximize_window()
	browser.get("https://ya.ru/")
	sleep(5)
	browser.save_screenshot("./ya_"+browser.name+".png")
	browser.quit()

make_screenshot(chrome)
make_screenshot(ff)


