from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://shop-frontend-8yko.onrender.com/")
assert "Shop" in driver.title
driver.quit()
