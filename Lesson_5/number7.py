from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
options=Options()

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/inputs")

search_input = driver.find_element(By.TAG_NAME, "input")
search_input.send_keys("1000")
sleep(5)
search_input.clear()
sleep(5)
search_input.send_keys("999")
sleep(5)

options.get("http://the-internet.herokuapp.com/inputs")

search_input1 = options  .find_element(By.TAG_NAME, "input")
search_input1.send_keys("1000")
sleep(5)
search_input1.clear()
sleep(5)
search_input1.send_keys("999")
sleep(5)