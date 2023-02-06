from googlesearch import search as sch
import pandas as pd

class DataSheet:
  def __init__(self,columns = [],load_path = None,load = False,repository = False,repository_path = ''):
    self.columns = columns
  

    #create_datasheet
    if load:
      self.datasheet = pd.read_csv(load_path)
      self.length = len(self.datasheet)
    else:
      self.datasheet = pd.DataFrame(columns = self.columns)
      self.length = len(self.datasheet)
     
    if repository:
      #load repository
      self.load_repository(repository_path)

  def load_repository(self,repository_path):
    with open(repository_path) as file: 
      self.repository = file

  def add_row(self,row):
    assert type(row) == list, "The row must be a list of items"
    self.datasheet.loc[self.length] = row
    self.length += 1

  def add_column(self,name,position,column_data):
    #the column data for each of the existing rows must be provided inside a list
    self.datasheet.insert(position,name,column_data,True)
  
  def show(self):
    display(self.datasheet)
  
  def remove_row(self,index):
    self.datasheet.drop(index,inplace = True)
    self.length -= 1
    self.datasheet.reset_index(inplace = True)

  def remove_column(self,remove_columns):
    self.datasheet.drop(columns = remove_columns,inplace = True)

  def remove_nan_on_row(self,row):
    pass

  def check_repository(self):
    pass
  
  def change_row(self,row_number,new_values):
    self.datasheet.loc[row_number] = new_values  
  
  def change_column(self):
    pass
  
  def change_entry(self,column,row,new_value):
    self.datasheet.loc[row,[column]] = [new_value]
  
  def check_nan(self):
    pass

  def to_csv(self,path):
    self.datasheet.to_csv(path)

#Search Class 

#let's write a quick class
from googlesearch import search as sch
import pandas as pd

class EasySearch:
  'The pandas and google search libraries are required'
  
  def __init__(self,queries:list,num = 1,start = 0,stop = 1,pause = 1):
    
    #To implement: add the datasheet to the DatasetSearch class to be able to manipulate it inside.
    
    self.queries = queries
    self.num,self.start, self.stop, self.pause = num,start,stop,pause

  
  def to_set(self):
    self.current_results = set()
    for query in self.queries: 
      for j in sch(query,num = self.num,start = self.start, stop = self.stop, pause = self.pause):
        self.current_results.add(j)


  def to_dict(self):
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
