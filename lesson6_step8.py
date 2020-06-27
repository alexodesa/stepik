from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	input1 = browser.find_element_by_tag_name('input')
	input1.send_keys("Alex")
	
	
	
finally:
	
	time.sleep(30)
	browser.quit()
	

