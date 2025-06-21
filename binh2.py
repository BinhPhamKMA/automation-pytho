from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Khởi tạo trình duyệt
driver = webdriver.Chrome()

# Mở trang login
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Chờ username xuất hiện & nhập
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
).send_keys("Admin")

# Chờ password xuất hiện & nhập
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
).send_keys("admin123")

# Chờ nút login khả dụng & click
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
).click()

# Chờ vào dashboard rồi kiểm tra
WebDriverWait(driver, 10).until(
    EC.url_contains("/dashboard")
)

print(" Đăng nhập thành công!")

# (Tùy chọn) Đóng trình duyệt sau vài giây
import time
time.sleep(3)
driver.quit()