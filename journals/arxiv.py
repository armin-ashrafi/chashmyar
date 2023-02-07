class ArxivScraper:
  def __init__(self,tags=[],driver_path = 'chromedriver',all_pages = False,base_url = 'https://arxiv.org'):
    self.article_repository = []
    self.tags = tags
    self.all_pages = all_pages
    

    #setup selenium driver
    self.scraper = ScrapingHandler(base_url,driver_path = driver_path) 

  def search_articles(self,query,repository = [], search_config = {'arxiv_url':'https://export.arxiv.org/find','size_button_xpath':"//select[@name='size']",
                                                         'results_per_page':'200','go_button_xpath':'//*[@id="main-container"]/div[2]/div[1]/div/form/div[2]/div[3]/button'}):
    
    self.article_repository = repository

    #print(search_config['arxiv_url'])
    self.scraper.reset_search()
    self.scraper.driver.get(search_config['arxiv_url'])
    
    select_size = Select(self.scraper.driver.find_element('name','per_page'))
    select_size.select_by_visible_text('100')
    #time.sleep(1)
    
    title_search = self.scraper.driver.find_element('name','query_2')
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
    self.paper_doi = [doi.text.split('[')[0] for doi in doien]
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
  
  def check_new_article(self):
    pass

if __name__ == '__main__':
  arxiv_search = ArxivScraper()
  
  #Example search with incomplete repository
  arxiv_search.search_articles('retinoblastoma',repository = ['https://arxiv.org/abs/2103.07622',
 'https://arxiv.org/abs/1911.00469',
 'https://arxiv.org/abs/1809.09161',
 'https://arxiv.org/abs/1809.09142',
 'https://arxiv.org/abs/1809.09073',
 'https://arxiv.org/abs/1407.4374',
 'https://arxiv.org/abs/0812.0160',
 'https://arxiv.org/abs/0809.2585',
 'https://arxiv.org/abs/0711.4743',
 'https://arxiv.org/abs/0711.0175',
 'https://arxiv.org/abs/0707.4321',
 'https://arxiv.org/abs/0707.4174',
 'https://arxiv.org/abs/0706.1996'])
  arxiv_search.check_new_doi()
  print(arxiv_search.novel_dois)


