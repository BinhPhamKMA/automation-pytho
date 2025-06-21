from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Khởi tạo trình duyệt
driver = webdriver.Chrome()
driver.maximize_window()

# Mở trang login
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
print(f"The web title is: {driver.title}")

# Mở Google
driver.get("https://www.google.com/")
print(f"The title of current page: {driver.title}")

# Quay lại trang trước
driver.back()
print(f"The title of current page: {driver.title}")

# Tiến tới trang tiếp theo
driver.forward()
print(f"The title of current page: {driver.title}")

# Đóng trình duyệt
driver.quit()