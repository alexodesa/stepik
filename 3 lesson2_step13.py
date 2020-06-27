from selenium import webdriver
import time
import unittest

browser = webdriver.Chrome()

try:


	class TestAbs(unittest.TestCase):
		def test_abs1(self):
		
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
			
			self.assertEqual('Congratulations! You have successfully registered!',congrats_text, 'error')
		
		
		def test_abs2(self):
		
		
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
			
			#self.assertEqual(abs(-42), -42, "Should be absolute value of a number")
        
	if __name__ == "__main__":
		unittest.main()


finally:
	time.sleep(3)
	browser.quit()
	
	# Empty line