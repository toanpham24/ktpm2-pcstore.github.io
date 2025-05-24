from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://shop-frontend-8yko.onrender.com/")
title = driver.title
print("Tiêu đề trang web:", title)  # In tiêu đề ra console
assert "Shop" in title  # Kiểm tra xem "Shop" có trong tiêu đề không
driver.quit()