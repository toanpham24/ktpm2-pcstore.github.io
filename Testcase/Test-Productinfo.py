from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class ShopPageTest(unittest.TestCase):
    def setUp(self):
        # Khởi tạo driver
        self.driver = webdriver.Chrome()
        self.driver.get("https://shop-frontend-8yko.onrender.com/")  # URL của trang

    def test_page_elements(self):
        # Kiểm tra tiêu đề sản phẩm
        product_title = self.driver.find_element(By.CLASS_NAME, "mb-3").text
        expected_title = "Tai nghe Sony WH-1000XM4"
        self.assertEqual(product_title, expected_title, f"Tiêu đề sản phẩm không khớp! Kỳ vọng: {expected_title}, Thực tế: {product_title}")
        print("Tiêu đề sản phẩm:", product_title)

        # Kiểm tra giá sản phẩm
        product_price = self.driver.find_element(By.XPATH, "//p[contains(text(), 'Stock')]").text
        expected_price = "Stock: 120"
        self.assertEqual(product_price, expected_price, f"Giá sản phẩm không khớp! Kỳ vọng: {expected_price}, Thực tế: {product_price}")
        print("Giá sản phẩm:", product_price)

        # Kiểm tra danh mục
        category = self.driver.find_element(By.XPATH, "//p[contains(text(), 'Category')]").text
        expected_category = "Category: Âm thanh"
        self.assertEqual(category, expected_category, f"Danh mục không khớp! Kỳ vọng: {expected_category}, Thực tế: {category}")
        print("Danh mục:", category)

        # Kiểm tra sự tồn tại của nút "Thêm vào giỏ hàng"
        add_to_cart_button = self.driver.find_element(By.CLASS_NAME, "btn-primary")
        self.assertTrue(add_to_cart_button.is_displayed(), "Nút 'Thêm vào giỏ hàng' không hiển thị!")
        self.assertEqual(add_to_cart_button.text, "Thêm vào giỏ hàng", "Nội dung nút không đúng!")
        print("Nút 'Thêm vào giỏ hàng' hiển thị với nội dung:", add_to_cart_button.text)

    def tearDown(self):
        # Đóng driver sau khi kiểm tra
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()