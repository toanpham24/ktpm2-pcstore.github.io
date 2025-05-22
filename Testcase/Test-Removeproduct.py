from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://shop-frontend-8yko.onrender.com/cart")
driver.find_element(By.CLASS_NAME, "remove-item").click()
assert "Your cart is empty" in driver.page_source
driver.quit()
