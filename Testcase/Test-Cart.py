from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://shop-frontend-8yko.onrender.com/cart")
assert "Your Cart" in driver.page_source
driver.quit()
