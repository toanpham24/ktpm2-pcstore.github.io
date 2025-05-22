from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://shop-frontend-8yko.onrender.com/login")
driver.find_element(By.NAME, "email").send_keys("123@gmail.com")
driver.find_element(By.NAME, "password").send_keys("123123")
driver.find_element(By.ID, "login-button").click()
assert "Welcome" in driver.page_source or "Logout" in driver.page_source
driver.quit()