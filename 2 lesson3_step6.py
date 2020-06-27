from selenium import webdriver
import time
import math

link="http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()

browser.get(link)

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	#found flight button and click on it
	fly_button = browser.find_element_by_xpath('//button[text()="I want to go on a magical journey!"]').click()
	
	# switch to another browser tab
	new_window = browser.window_handles[1]
	browser.switch_to.window(new_window)
	
	#copy text from element
	value = browser.find_element_by_id ('input_value')
	x = value.text
	y = calc(x)
	
	#find input field by id and fill in 'y'
	input_field = browser.find_element_by_id('answer')
	input_field.send_keys(y)
	
	# find submit button and click
	sumbit_button = browser.find_element_by_css_selector ('button.btn.btn-primary').click()
	
	# find alert
	alert = browser.switch_to.alert
	alert_text = alert.text
	print(alert_text)
	
	
	#alert.accept()
	
finally:
	time.sleep(15)
	browser.quit()
	
	#empty line