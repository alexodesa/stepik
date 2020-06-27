from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link ="http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()

try:
	browser.get(link)
	# Находим первый элемент
	element_num1 = browser.find_element_by_id("num1")
	x = element_num1.text
	
	#Находим второй элемент
	element_num2 = browser.find_element_by_id("num2")
	y = element_num2.text
	
	#Находим сумму двух элементов
	sum = int(x)+int(y)
	sum_str = str(sum)
	print("sum: ", sum)
	
	#Находим и открываем дропдаун
	#dropdown_open = browser.find_element_by_id('dropdown')
	#dropdown_open.click()
	
	#Альтернативный посик и нажатие
	#dropdown_open = browser.find_element_by_tag_name("select").click()
	
	
	#Есть более удобный способ, для которого используется специальный класс Select из библиотеки WebDriver.
	#Вначале мы должны инициализировать новый объект, передав в него WebElement с тегом select.
	#Далее можно найти любой вариант из списка с помощью метода select_by_value(value):

	#from selenium.webdriver.support.ui import Select
	#select = Select(browser.find_element_by_tag_name("select"))
	#select.select_by_value("1") # ищем элемент с текстом "Python"
	#Можно использовать еще два метода: 
	#select.select_by_visible_text("text") и select.select_by_index(index). 
	#Первый способ ищет элемент по видимому тексту, например, select.select_by_visible_text("Python") найдёт "Python" для нашего примера.

	#Второй способ ищет элемент по его индексу или порядковому номеру. Индексация начинается с нуля. 
	#Для того чтобы найти элемент с текстом "Python", нужно использовать select.select_by_index(1), 
	#так как опция с индексом 0 в данном примере имеет значение по умолчанию равное "--".
	
	#Инициализируем select и находим элемент по тегу select. 
	select = Select(browser.find_element_by_tag_name("select"))
	#Находим элемент с нужным значением и кликаем
	select.select_by_value(sum_str) # ищем элемент с текстом равным sum
	
	
	btn = browser.find_element_by_css_selector('button.btn')
	btn.click()
	
	
	
	
	
	
	
finally:
	time.sleep(5)
	browser.quit()
	
	# leave one empty line