from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://shop-frontend-8yko.onrender.com/cart")
driver.find_element(By.ID, "checkout").click()
# Giả định có form thanh toán
driver.find_element(By.ID, "submit-order").click()
assert "Order confirmed" in driver.page_source
driver.quit()
