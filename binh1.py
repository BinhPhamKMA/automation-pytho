import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Launch the brower 
driver = webdriver.Chrome()

#navigator to google 
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
sleep(5)

#Login 
driver.find_element(By.NAME, "username").click()
driver.find_element( By.NAME,"username").send_keys("Admin")
driver.find_element( By.NAME, "password").send_keys("admin123")




