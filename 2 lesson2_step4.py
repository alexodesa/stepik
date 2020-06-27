#from selenium import webdriver
#browser = webdriver.Chrome()
#browser.execute_script("alert('Robots at work');")
#browser.execute_script("document.title='Script executing';")
#browser.execute_script("document.title='Script executing';alert('Robots at work');")

#from selenium import webdriver

#browser = webdriver.Chrome()
##link = "https://SunInJuly.github.io/execute_script.html"
#browser.get(link)
#button = browser.find_element_by_tag_name("button")
#browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#button.click()
#assert True


from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()

# Посчитать математическую функцию от x.
def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	# Открыть страницу http://SunInJuly.github.io/execute_script.html.
	browser.get(link)
	
	#Считать значение для переменной x.
	#Находим элемент с х
	text1 = browser.find_element_by_css_selector('#input_value')
	x = text1.text
	y = calc(x)

	
	#Находим поле ввода и вставляем туда 'y'
	input_field = browser.find_element_by_id ('answer')
	input_field.send_keys(y)
	
	#Проскроллить страницу вниз до видимости кнопки Submit.
	button = browser.find_element_by_tag_name("button")
	browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	
	#Найдем чекбокс robotCheckbox и клацнем на него
	robotCheckbox = browser.find_element_by_id('robotCheckbox')
	robotCheckbox.click()
	
	# Переключим радиобаттан robotsRule
	robotsRule = browser.find_element_by_id('robotsRule')
	robotsRule.click()
	
	button.click()
	
	
	
	
finally:
	time.sleep(5)
	browser.quit()
	
#Leave empty line