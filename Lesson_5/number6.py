from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import FirefoxDriverManager

driver1 = webdriver.Firefox(service=FirefoxService(FirefoxDriverManager().install))

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/entry_ad")

driver.find_element(By.PARTIAL_LINK_TEXT, '$0').click()

#нашла как вызвать этот локатор в браузере, теперь вопрос в том как его вызвать через Visual Studio

sleep(5)