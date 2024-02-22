from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

for x in range(1, 6):
    driver.find_element(By.TAG_NAME, "button").click()

print(len(driver.find_elements(By.CLASS_NAME, "button.added-manually")))

#почему-то не получается вывести список; мне кажется это из-за тега: button

sleep(5)