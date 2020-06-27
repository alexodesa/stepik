from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


link='http://suninjuly.github.io/explicit_wait2.html'
def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))



try:
	browser = webdriver.Chrome()
	browser.get(link)
	browser.implicitly_wait(5)
	
	
	
	# Ждем 12 секунд и проверяем постоянно (каждые 0.5сек ), что значение элемента с ID price равно $100
	# Делается это только с конструкцией BY.ID
	price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
	# Как только стало равно, делаем следющий шаг
	# жмем Book
	button = browser.find_element_by_id ('book').click()
	
	
	# Ищем число
	value = browser.find_element_by_id('input_value')
	x = value.text
	y = calc(x)

	# Ищем инпут строку и вставляем "х"
	input = browser.find_element_by_id('answer')
	input.send_keys(y)
	
	# Ищем и жмем кнопку submit
	submit = browser.find_element_by_id('solve')
	submit.click()
	
finally:
	time.sleep(5)
	browser.quit()
	
#Leave empty line
	