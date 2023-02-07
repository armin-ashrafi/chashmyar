from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup as bs
import time

class ScrapingHandler:
  
  
  def __init__(self,base_url,driver_path = 'chromedriver'):
    self.add_driver_arguments(arguments = ['--headless','--no-sandbox'])
    self.driver_path = driver_path
    self.base_url = base_url

    #super().__init__(self,self.driver_path,options = self.options)
    #self.driver = web
    
    self.set_driver()
    self.get_soup()



  def add_driver_arguments(self,arguments = ['--headless','--no-sandbox']):
    self.options = Options()
    for argument in arguments:
      self.options.add_argument(argument)
  
  def set_driver(self):
    ''' it (re)sets the driver. '''
    self.add_driver_arguments()
    self.driver = webdriver.Chrome(self.driver_path,options = self.options)

  def reset_search(self):
    self.driver.get(self.base_url)
  
  def get_soup(self,parser = 'lxml'):
    '''gets the soup of the current webpage in the driver '''
    self.soup = bs(self.driver.page_source,parser)
