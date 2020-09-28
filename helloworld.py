import selenium
from selenium import webdriver
driver = webdriver.Chrome(executable_path='./chromedriver')
print(type(driver),driver)
# <class 'selenium.webdriver.chrome.webdriver.Webdriver.WebDriver'><sel...(session="2...>
driver.get(url="http://www.google.com/")
print(type(driver.page_source),driver.page_source)
# <class 'str'>'<html itemscope=""...</body></html>'
driver.quit()
