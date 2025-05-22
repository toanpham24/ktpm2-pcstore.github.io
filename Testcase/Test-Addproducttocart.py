from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://shop-frontend-8yko.onrender.com/")
driver.find_element(By.CSS_SELECTOR, ".product-item a").click()
driver.find_element(By.ID, "add-to-cart").click()
assert "1" in driver.find_element(By.ID, "cart-count").text
driver.quit()
