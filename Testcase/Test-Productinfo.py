from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://shop-frontend-8yko.onrender.com/")
product = driver.find_element(By.CSS_SELECTOR, ".product-item a")
product.click()
assert "Description" in driver.page_source or "Price" in driver.page_source
driver.quit()