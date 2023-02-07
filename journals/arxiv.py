class ArxivScraper:
  def __init__(self,tags=[],driver_path = 'chromedriver',all_pages = False,base_url = 'https://arxiv.org'):
    self.article_repository = []
    self.tags = tags
    self.all_pages = all_pages
    

    #setup selenium driver
    self.scraper = ScrapingHandler(base_url,driver_path = driver_path) 

 
  def search_articles(self,query,repository = [], search_config = {'arxiv_url':'https://export.arxiv.org/find','size_button_name':"per_page",
                                                         'results_per_page':'100','title_search_name':'query_2'}):
    
    self.article_repository = repository

    #print(search_config['arxiv_url'])
    self.scraper.reset_search()
    self.scraper.driver.get(search_config['arxiv_url'])
    
    select_size = Select(self.scraper.driver.find_element('name',search_config['size_button_name']))
    select_size.select_by_visible_text(search_config['results_per_page'])
    #time.sleep(1)
    
    title_search = self.scraper.driver.find_element('name',search_config['title_search_name'])
    title_search.send_keys(query)
    title_search.send_keys(Keys.RETURN)
          


  def get_paper_titles(self,find_config = {'class':'list-title mathjax'}):
    ''' '''
    self.scraper.get_soup()
    titles = self.scraper.soup.find_all('div',find_config) 
    self.titles = [title.text.strip()[7:] for title in titles]
    return self.titles

  def get_paper_authors(self,find_config = {'class':'list-authors'}):  
    #setup the author search
    self.scraper.get_soup()
    authors = self.scraper.soup.find_all('div',find_config) 
    self.authors = [author_group.text.strip[8:].replace('\n','').split(',') for author_group in authors]
    return self.authors

  
  def get_paper_tags(self,find_config = {'class':'list-subjects'}):  
    self.scraper.get_soup()
    tags = self.scraper.soup.find_all('div',find_config)
    self.tags = [tag.text.strip()[9:].split(';') for tag in tags]
    return self.tags

  def get_paper_doi(self,find_config = {'class':'list-identifier'}):
    self.scraper.get_soup()
    doien = self.scraper.soup.find_all('span',find_config)
    self.paper_doi = [doi.text.split('[')[0].strip() for doi in doien]
    return self.paper_doi

  def check_new_doi(self):
    ''' Checks if there are new dois that are not in the repository '''
    self.novel_dois = []
    self.get_paper_doi()
    if len(self.article_repository) == 0:
      raise ValueError('No repository was provided')
    #print(self.paper_doi)
    
    for doi in self.paper_doi:
      if doi not in self.article_repository:
        self.novel_dois.append(doi)
    
    #print('hello!')
    
    if len(self.novel_dois) != 0:
      return True
    
    return False        
  
  def get_lean_tags(self):
    '''Create a list of lean tags that are searchable'''
    self.get_paper_tags()
    
    self.lean_tags = []
    for tags in self.tags:
      lean_tag_group = []
      for tag in tags:
        lean_tag = tag.split('(')[1][:-1]
        lean_tag_group.append(lean_tag)
      self.lean_tags.append(lean_tag_group)
    return self.lean_tags

if __name__ == '__main__':
  arxiv_search = ArxivScraper()
  
  #Example search with incomplete repository
  arxiv_search.search_articles('retinoblastoma')
  print(arxiv_search).get_paper_titles()
