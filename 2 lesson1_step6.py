from selenium import webdriver
import time

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

try:
	#Найдем радиобаттон
	people_radio = browser.find_element_by_id("peopleRule")
	# Найдем атрибут checked с помощью get_attribute
	
	people_checked = people_radio.get_attribute("checked")
	print("value of people radio: ", people_checked)
	assert people_checked is not None, "People radio is not selected by default"
	
	robots_radio = browser.find_element_by_id("robotsRule")
	robots_checked = robots_radio.get_attribute("checked")
	assert robots_checked is None
	
	# Find submit button 
	submit_button = browser.find_element_by_xpath('//button[text()="Submit"]')
	
	# Checked 'disable' attribute is absent
	sumbit_disabled = submit_button.get_attribute("disabled")
	print("Disabled is present?: ", sumbit_disabled)
	assert sumbit_disabled is None, "Кнопка не активна"
	
	time.sleep(13)
	
	# Checked 'disable' is appeared after timeout of 10 sec 
	# Find Submit button
	
	sumbit_button = browser.find_element_by_css_selector(".btn")
	submit_enabled = submit_button.get_attribute("disabled")
	print("Disabled is present?: ", submit_enabled)
	
	#Проверка. Если submit_enabled БУДЕТ! равна None,а не true, то вылезет ошибка: "Кнопка еще аквтина"/  Можно поиграть с паузой
	assert submit_enabled is not None, "Кнопка еще аквтина"
	
	
finally:
	time.sleep(1)
	browser.quit()
	
# не забываем оставить пустую строку в конце файла
	
