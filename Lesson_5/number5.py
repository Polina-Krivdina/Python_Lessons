from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

for x in range(1, 4):
    driver.get("http://uitestingplayground.com/classattr")
    driver.find_element(By.CSS_SELECTOR, "button.btn-primary").click()
    sleep(10)

sleep(5)