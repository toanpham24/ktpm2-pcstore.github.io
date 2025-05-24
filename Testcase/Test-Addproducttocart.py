from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Khởi tạo driver
driver = webdriver.Chrome()

# Truy cập trang chính
driver.get("https://shop-frontend-8yko.onrender.com/")  # URL của trang chính

# Tìm và nhấn vào liên kết chi tiết sản phẩm
product_link = driver.find_element(By.XPATH, "//span[text()='Tai nghe Sony WH-1000XM4']/parent::a")
product_link.click()
print("Đã truy cập vào trang chi tiết sản phẩm")

# Chờ trang chi tiết tải (có thể cần điều chỉnh thời gian)
time.sleep(2)

# Tìm và nhấn nút "Thêm vào giỏ hàng" trên trang chi tiết
add_to_cart_button = driver.find_element(By.CLASS_NAME, "btn-primary")
print("Nút 'Thêm vào giỏ hàng' trước khi nhấn:", add_to_cart_button.text)

# Kiểm tra nút có hiển thị và có thể nhấn được không
assert add_to_cart_button.is_displayed(), "Nút 'Thêm vào giỏ hàng' không hiển thị!"
assert add_to_cart_button.is_enabled(), "Nút 'Thêm vào giỏ hàng' không thể nhấn!"
add_to_cart_button.click()
print("Đã nhấn nút 'Thêm vào giỏ hàng'")

# Đợi một chút để trang phản hồi
time.sleep(2)

# Kiểm tra phản hồi (giả sử có thông báo thành công)
try:
    success_message = driver.find_element(By.CLASS_NAME, "success-message")  # Giả định có thông báo
    print("Thông báo sau khi thêm:", success_message.text)
except:
    print("Không tìm thấy thông báo thành công, kiểm tra xem chức năng có hoạt động không.")

# Đóng driver
driver.quit()