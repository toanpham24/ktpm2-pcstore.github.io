from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://shop-frontend-8yko.onrender.com/")
search_box = driver.find_element(By.NAME, "search")
search_box.send_keys("Shoes")
search_box.send_keys(Keys.RETURN)
assert "Shoes" in driver.page_source
driver.quit()
