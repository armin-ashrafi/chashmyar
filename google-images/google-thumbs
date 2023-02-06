import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import base64


options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
driver = webdriver.Chrome('chromedriver',options = options)


#Setup cookies

def setup_cookies():
  driver.get('https://google.com')
  for cookie in driver.get_cookies():
    driver.delete_cookie(cookie['name'])
  driver.add_cookie({'domain': '.google.com', 'expiry': 1738751313, 'httpOnly': False, 
                       'name': 'CONSENT', 'path': '/', 'secure': True, 'value': 'YES+'}) #it accepts "Yes+"


def scroll_to_end(sleep = 5):
    #driver.execute_script('window.scrollBy(0,{})'.format(scroll_height))
    driver.find_element('css selector','body').send_keys(Keys.CONTROL, Keys.END)
    time.sleep(sleep)


def get_google_thumbnails(keyword,output_path,scroll_number = 5,scroll_sleep = 5):
  setup_cookies()
  image_b64 = []
  image_https = []
  
  for _ in range(scroll_number):
    scroll_to_end(scroll_sleep)

    driver.get('https://google.com/imghp')
    search = driver.find_element('name','q')
    search.send_keys(keyword)
    search.send_keys(Keys.RETURN)
    time.sleep(1)

    image_elements = driver.find_elements('class name','rg_i')
    image_sources =   [element.get_attribute('src') for element in image_elements if element.get_attribute('src') is not None]

    #We now have the base64 elements, we can proceed to making them into bytes and saving them on the drive:
    
    for image in image_sources:
      try:
        image_b64.append(image.split('data:image/jpeg;base64,')[1])
      except:
          pass
    #make into bytes:
    image_bytes_list = [base64.b64decode(image) for image in image_b64]

    #make them into individual files
    for index,byte in enumerate(image_bytes_list):
      with open(output_path + '{}.jpg'.format(index),'wb') as img:
        img.write(byte)
  
  for index,image in enumerate(image_https):
    get_image = requests.get(image).content
    with open(output_path +'{}.jpg'.format(file_number),'wb') as img:
      img.write(get_image)
    file_number += 1



if __name__ == '__main__':
	get_google_thumbnails('Trump Tower','')
