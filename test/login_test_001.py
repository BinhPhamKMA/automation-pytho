import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.read_config import ConfigReader
import time
@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(ConfigReader.get_timeout())
    driver.get(ConfigReader.get_base_url())
    yield driver
    driver.quit()

def test_login_successfull(driver):
    # 1. Go to page
    driver.get(ConfigReader.get_base_url())
    time.sleep(10)

    # 2. Verify that dispatch field username, pw
    username_field = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, "username")))
    password_field = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, "password")))
    time.sleep(1)
    # 3. Fill username pw
    username_field.send_keys(ConfigReader.get_username())
    password_field.send_keys(ConfigReader.get_password())
    time.sleep(5)
    # Click Login button
    login_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login_button.click()
    #4. Verify that Dashboard
    dashboard_header = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".oxd-text--h6")) )
    assert "Dashboard" in dashboard_header.text, "Management page not displayed"

    # 5. Verify Recruitment menu
    recruitment_menu = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//span[text()='Recruitment']"))
    )
    assert recruitment_menu.is_displayed(), "Recruitment menu not displayed"

    # 6. Logout
    profile_dropdown = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "oxd-userdropdown-tab"))
    )
    profile_dropdown.click()

    logout_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']"))
    )
    logout_button.click()

    # 7. Verify login page appears again
    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.NAME, "username"))
    )
