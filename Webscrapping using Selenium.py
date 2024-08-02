from selenium import webdriver

website = "https://www.bbc.com/sport/football"

driver = webdriver.Chrome()
driver.get(website)
driver.quit()