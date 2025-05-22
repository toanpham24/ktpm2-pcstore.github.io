from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://shop-frontend-8yko.onrender.com/register")
driver.find_element(By.NAME, "name").send_keys("Test User")
driver.find_element(By.NAME, "email").send_keys("testuser@example.com")
driver.find_element(By.NAME, "password").send_keys("TestPass123")
driver.find_element(By.NAME, "confirmPassword").send_keys("TestPass123")
driver.find_element(By.ID, "register-button").click()
assert "Welcome" in driver.page_source or "Home" in driver.title
driver.quit()
