from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Tạo dữ liệu ngẫu nhiên hợp lệ
rand = random.randint(1000, 9999)
full_name = f"Test User {rand}"

# Số điện thoại 10 số
phone_prefix = random.choice(["090", "091", "092", "093", "094", "095", "096", "097", "098", "099"])
phone_suffix = random.randint(1000000, 9999999)
phone = f"{phone_prefix}{phone_suffix}"

address = f"123 Đường Test {rand}"
email = f"test{rand}@example.com"
password = "Test@1234"

# Khởi chạy trình duyệt
driver = webdriver.Chrome()

try:
    # 1. Mở trang chính
    driver.get("https://shop-frontend-8yko.onrender.com/")

    # 2. Click nút "Đăng nhập"
    login_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Đăng nhập']/parent::a"))
    )
    login_btn.click()

    # 3. Chuyển sang trang "Đăng ký"
    register_span = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Chưa có tài khoản? Đăng ký')]"))
    )
    register_span.click()

    # 4. Đợi input hiện ra
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "form-control"))
    )

    # 5. Nhập thông tin
    inputs = driver.find_elements(By.CLASS_NAME, "form-control")
    inputs[0].send_keys(full_name)   # Họ và tên
    inputs[1].send_keys(phone)       # Số điện thoại
    inputs[2].send_keys(address)     # Địa chỉ
    inputs[3].send_keys(email)       # Email
    inputs[4].send_keys(password)    # Mật khẩu

    # 6. Gửi form
    register_button = driver.find_element(By.CLASS_NAME, "btn-primary")
    register_button.click()

    # 7. Kiểm tra kết quả bằng Toastify
    toast = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "Toastify"))
    )
    print(f"✅ Đăng ký thành công:\n - SĐT: {phone}\n - Email: {email}\n - Mật khẩu: {password}")


except Exception as e:
    print(f"❌ Kiểm thử thất bại: {e}")

finally:
    time.sleep(5)
    driver.quit()
