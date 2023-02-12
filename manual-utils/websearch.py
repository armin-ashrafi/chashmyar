#Search Class 
#!pip install -U duckduckgo_search
from duckduckgo_search import ddg
#let's write a quick class
from googlesearch import search as sch
import pandas as pd

def duckduckgo_search_func(num = 1,start = 0,stop = 1,pause = 1):
  ''' It searches the google search engine for results '''
  search_results = set()
  for j in sch(query,num = self.num,start = self.start, stop = self.stop, pause = self.pause):
        search_results.add(j)
  return search_results
  

class EasySearch:
  'The pandas and google search libraries are required'
  
  def __init__(self,queries:list):
    self.queries = queries
    self.current_results = []
    

  def google_to_set(self,search_engine = 'google',num = 1,start = 0,stop = 20,pause = 5):
    '''puts all the results into a set where there are no repetitions '''
    self.current_results = set()
    for query in self.queries: 
      for j in sch(query,num = num,start = start, stop = stop, pause = pause):
        self.current_results.add(j)

  
  def ddg_to_set(self,num_pages = 5,new_check = True):
    new_results = set()
    pages = [ddg(query,num_pages) for query in self.queries]
    for page in pages:
      for hit in page:
        new_results.add(hit['href'])
    
    if new_check:
      diff = new_results.difference(self.current_results)
      
      if len(diff) != 0:
        self.new_results = diff
        return True
      
      return False


  def google_to_dict(self):
    ''' This will contain duplicate answers'''
    self.current_results = dict()
    for query in self.queries:
      results = set()
      for j in sch(query, num = self.num,start = self.start, stop = self.stop, pause = self.pause):
        results.add(j)
        self.current_results[query] = results


  def narrow_set(self,keyword):
    self.current_narrow = []
    for result in self.current_results:
      if keyword in result:
        self.current_narrow.append(result)

  def set_params(self,new_values):
    self.num,self.stop,self.pause = new_values

  def set_queries(self,queries):
    self.queries = queries

  def save_results_to_datasheet(self,datasheet):
    pass

  def clear_currents(self):
    self.current_narrow = []
    self.current_results = []
    
    
if __name__ == '__main__':
  my_search = EasySearch(['retinoblastoma'])
  my_search.google_to_set(num = 10,stop = 50,pause =5)
  my_search.ddg_to_set(num_pages = 50) #DuckDuckgo is significantly faster than google, because of ease of access
