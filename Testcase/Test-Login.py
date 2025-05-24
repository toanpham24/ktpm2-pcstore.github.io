from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Khởi tạo trình duyệt
driver = webdriver.Chrome()

try:
    # Truy cập trang chính
    driver.get("https://shop-frontend-8yko.onrender.com/")

    # Click vào nút "Đăng nhập"
    login_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Đăng nhập']/parent::a"))
    )
    login_link.click()

    # Đợi form đăng nhập hiển thị
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "form-control"))
    )

    # Lấy danh sách input (email, password)
    inputs = driver.find_elements(By.CLASS_NAME, "form-control")
    email_input = inputs[0]
    password_input = inputs[1]

    # Nhập thông tin đăng nhập
    email_input.send_keys("123@gmail.com")
    password_input.send_keys("123123")

    # Click nút "Đăng nhập"
    driver.find_element(By.CLASS_NAME, "btn-primary").click()

    # Đợi xem có toast message hoặc chuyển hướng
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "Toastify"))
    )

    print("✅ Đăng nhập thành công!")

except Exception as e:
    print("❌ Kiểm thử thất bại:", e)

finally:
    time.sleep(5)  # Để quan sát kết quả
    driver.quit()
