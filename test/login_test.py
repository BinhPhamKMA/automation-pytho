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

def test_add_vacancy_flow(driver):
    # 1. Vào trang và login
    driver.get(ConfigReader.get_base_url())
    time.sleep(10)

    # Đợi Username và Password field hiển thị
    username_field = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, "username")))
    password_field = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, "password")))
    time.sleep(1)
    # Nhập thông tin đăng nhập
    username_field.send_keys(ConfigReader.get_username())
    password_field.send_keys(ConfigReader.get_password())
    time.sleep(5)
    # Click Login button
    login_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login_button.click()

    dashboard_header = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".oxd-text--h6")) )
    assert "Dashboard" in dashboard_header.text, "Management page not displayed"

    # 2. Click Recruitment > Vacancies tab
    recruitment_menu = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Recruitment']")))
    recruitment_menu.click()

    vacancies_tab = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'oxd-topbar-body-nav-tab-item') and normalize-space(text())='Vacancies']")))
    vacancies_tab.click()

    # 3. Click "+ Add" button
    add_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,' Add ')]")))
    add_button.click()

    # 4. Verify Add Vacancy page hiển thị (ví dụ check header hoặc tiêu đề)
    header = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//h6[contains(text(),'Add Vacancy')]")))
    assert header.is_displayed()

