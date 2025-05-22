from selenium import webdriver
from selenium.webdriver.chrome.options import Options

mobile_emulation = { "deviceName": "iPhone X" }
chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://shop-frontend-8yko.onrender.com/")
assert "Menu" in driver.page_source or "burger icon" in driver.page_source
driver.quit()
