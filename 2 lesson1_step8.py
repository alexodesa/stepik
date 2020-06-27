from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	browser.get(link)
	
	text1 = browser.find_element_by_id('treasure')
	text1_1 = text1.get_attribute("valuex")
	x = text1_1
	y = calc(x)
	
	input_field = browser.find_element_by_css_selector('input#answer:required')
	input_field.send_keys(y)
	
	check_box = browser.find_element_by_css_selector('#robotCheckbox')
	check_box.click()
	
	radio_button = browser.find_element_by_id('robotsRule')
	radio_button.click()
	
	submit = browser.find_element_by_xpath('//button[text() = "Submit"]')
	submit.click()
	
finally:
	time.sleep(10)
	