import wget
import urllib.request
import selenium
from selenium import webdriver
driver = webdriver.Chrome(executable_path='./chromedriver')

from selenium.webdriver.common.by import By

url='http://www.coupang.com/np/search?q=컴퓨터' #as http 200
driver.get(url=url)
elements=driver.find_elements(By.XPATH,'//img[@class="search-product-wrap-img"]')
down_path='pictures/'
for element in elements:
    src = element.get_attribute('src')
    #download the image
    img_txt = src.split('/')[-1]
    image_name=down_path+img_txt
    #first way
    #wget.download(url=src, out=image_name) #HTTP Error 403: Forbidden
    #second way
    #Download the file from 'url' and save it locally inder 'file_name':
    with urlib.request.urlopen(src) as response, open(image_name,'wb') as out_file:
        data = response.read() # a 'bytes' object
        out_file.write(data)