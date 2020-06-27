from selenium import webdriver
import time
import math

link = 'http://suninjuly.github.io/alert_accept.html'

browser = webdriver.Chrome()

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

# Open page
browser.get(link)

try:

	#Find button and click
	button = browser.find_element_by_xpath ("//button[text()='I want to go on a magical journey!']").click()
	
	#Target on Alert and accept it
	alert = browser.switch_to.alert
	alert.accept()
	
	#Find element and copy it
	value = browser.find_element_by_id('input_value')
	#Берем текст из тега, который нашли выше
	x= value.text
	y = calc(x)
	
	#Find input field
	
	input = browser.find_element_by_name ('text')
	# Отправляем туда 'y'
	input.send_keys(y)
	
	# Find Submit button and click
	submit_button = browser.find_element_by_css_selector ('button[type="submit"]').click()
	
	
	
finally:
	time.sleep(5)
	browser.quit()
	
	#leave one string
	