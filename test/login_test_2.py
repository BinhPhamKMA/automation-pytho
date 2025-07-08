import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.read_config import ConfigReader


@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # 👉 Bỏ comment nếu chạy không giao diện
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(ConfigReader.get_timeout())
    yield driver
    driver.quit()


def test_add_vacancy_flow(driver):
    driver.get(ConfigReader.get_base_url())
    time.sleep(3)

    # 1. Login
    username_field = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, "username")))
    password_field = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, "password")))

    username_field.send_keys(ConfigReader.get_username())
    password_field.send_keys(ConfigReader.get_password())

    login_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login_button.click()

    # 2. Xác nhận dashboard
    dashboard_header = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".oxd-text--h6"))
    )
    assert "Dashboard" in dashboard_header.text, "❌ Không load được Dashboard"

    # 3. Click Recruitment > Vacancies
    recruitment_menu = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Recruitment']"))
    )
    recruitment_menu.click()

    vacancies_tab = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@class, 'oxd-topbar-body-nav-tab-item') and normalize-space(text())='Vacancies']"))
    )
    vacancies_tab.click()

    # 4. Click "+ Add" button
    add_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(.,' Add ')]"))
    )
    add_button.click()

    # 5. Kiểm tra xem đã vào trang Add Vacancy chưa
    print("⏳ Checking Add Vacancy header...")

    # In URL để xác minh
    print(" Current URL:", driver.current_url)

