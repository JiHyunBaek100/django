import selenium
from selenium import webdriver
driver = webdriver.Chrome(executable_path='./chromedriver')


from selenium.webdriver.common.by import By


driver.get(url="https://www.google.com/")

from selenium.webdriver.common.keys import Keys
# enter "webdriver" text and perform "ENTER" keyboard action
driver.find_element(By.NAME,"q").send_keys("selenium"+Keys.ENTER)

SearchInput = driver.find_element(By.NAME,"q")
SearchInput.send_keys("selenium")
#Clears the entered text
SearchInput.clear()
