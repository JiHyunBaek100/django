import selenium
from selenium import webdriver
driver = webdriver.Chrome(executable_path='./chromedriver')

driver.get(url="http://www.google.com/")
from selenium.webdriver.common.by import By
search_form=driver.find_element(By.TAG_NAME,"form") #Find Element
print(type(search_form),search_form)
#<class 'selenium.webdriver.remote.webelement.WebElement'>...

search_box = search_form.find_element(By.NAME,"q") # find it from element
search_box.send_keys("webdriver")
#<class 'selenium.webdriver.remote.webelement.WebElement'>... #꼭 print()


#find Element from elements
driver.get(url="http://www.google.net/search?q=webdriver")
elements = driver.find_elements(By.XPATH,'//a[@href]')
#<class 'list'>[<selenium.sebdriver. ..., -8638-2f7617332c69")>]
for e in elements:
    if e != None:
       print(type(e.text),repr(e.text))
      #<class'str'><a ...



