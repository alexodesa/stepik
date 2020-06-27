from selenium import webdriver
import time

def test_1():
	
	try:
		browser = webdriver.Chrome()
		link = 'http://suninjuly.github.io/registration1.html'
		browser.get(link)
	
		# Находим First Name 
		first_name = browser.find_element_by_css_selector ('[placeholder="Input your first name"]:required')
		first_name.send_keys('Alex')
	
		# Нахожу last name
		last_name = browser.find_element_by_css_selector('[placeholder="Input your last name"]:required')
		last_name.send_keys('Vyder')
	
		# Нахожу Email
		email = browser.find_element_by_css_selector ('[placeholder="Input your email"]:required')
		email.send_keys('test@gmail.com')
		
		# Sumbit button find and execute
		submit = browser.find_element_by_xpath ('//button').click()
	
		# Берем текст с помощью get_attribute 
		# <h1>Congratulations! You have successfully registered!</h1>
		congrats = browser.find_element_by_xpath ('//h1')
		congrats_text = congrats.text
	
		assert congrats_text == 'Congratulations! You have successfully registered!', f"I have: {congrats_text}'"
		
	finally:
		time.sleep(1)
		browser.quit()
		
		#empty line
	
def test_2():
	
	try:
		browser = webdriver.Chrome()
		link = 'http://suninjuly.github.io/registration2.html'
		browser.get(link)
	
		# Находим First Name 
		first_name = browser.find_element_by_css_selector ('[placeholder="Input your first name"]:required')
		first_name.send_keys('Alex')
	
		# Нахожу last name
		last_name = browser.find_element_by_css_selector('[placeholder="Input your last name"]:required')
		last_name.send_keys('Vyder')
	
		# Нахожу Email
		email = browser.find_element_by_css_selector ('[placeholder="Input your email"]:required')
		email.send_keys('test@gmail.com')
		
		# Sumbit button find and execute
		submit = browser.find_element_by_xpath ('//button').click()
	
		# Берем текст с помощью get_attribute 
		# <h1>Congratulations! You have successfully registered!</h1>
		congrats = browser.find_element_by_xpath ('//h1')
		congrats_text = congrats.text
	
		assert congrats_text == 'Congratulations! You have successfully registered!', f"I have: {congrats_text}'"
		
	finally:
		time.sleep(1)
		browser.quit()
		
		#empty line