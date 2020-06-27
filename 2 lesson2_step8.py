from selenium import webdriver
import time
import os 

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

try:
	browser.get(link)
	
	#find and Fill out first name
	input1 = browser.find_element_by_name('firstname')
	input1.send_keys('test')
	
	#Found and filled in Last name
	input_last_name = browser.find_element_by_name('lastname')
	input_last_name.send_keys('Last Name')
	
	#Found and filled in email
	email = browser.find_element_by_name ('email')
	email.send_keys('email@test.com')
	
	
	element = browser.find_element_by_name ('file')
	current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
	file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
	element.send_keys(file_path)
	
	#Find and click Sumbit
	
	submit = browser.find_element_by_xpath ('//button[text()="Submit"]').click()
	
	
	
finally:
	time.sleep(5)
	browser.quit()
	
	#leave one empty string
	