from selenium import webdriver

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд


browser.get("http://suninjuly.github.io/cats.html")

button = browser.find_element_by_id("button")


