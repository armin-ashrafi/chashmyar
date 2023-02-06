class ArxivScraper:
  def __init__(self,tags=[],driver_path = 'chromedriver',all_pages = False,base_url = 'https://arxiv.org'):
    self.article_repository = []
    self.tags = tags
    self.all_pages = all_pages
    

    #setup selenium driver
    self.scraper = ScrapingHandler(base_url,driver_path = driver_path) 

  def search_articles(self,query,repository = [], search_config = {'arxiv_url':'https://arxiv.org','size_button_xpath':"//select[@name='size']",
                                                         'results_per_page':'200','go_button_xpath':'//*[@id="main-container"]/div[2]/div[1]/div/form/div[2]/div[3]/button'}):
    
    ''' gets the query, and depending on the page, it creates '''
    self.article_repository = repository

    #print(search_config['arxiv_url'])
    self.scraper.reset_search()
    self.scraper.driver.get(search_config['arxiv_url'])
    #self.scraper.save_screenshot('arminska.jpg')
    
    #Find search bar, send in the query and press return
    search_bar = self.scraper.driver.find_element('name','query')
    #print(search_bar)
    
    search_bar.send_keys(query)
    search_bar.send_keys(Keys.RETURN)
    
    #wait for page to load(might need to be replaced with implicit wait)
    time.sleep(1)

    #Arxiv has various results per page options, by default we would like to use the most number available:
    select_size = Select(self.scraper.driver.find_element('xpath',search_config['size_button_xpath']))
    select_size.select_by_value(search_config['results_per_page'])
    button = self.scraper.driver.find_element('xpath',search_config['go_button_xpath'])
    button.click()

  def get_paper_titles(self,find_config = {'class':'title is-5 mathjax'}):
    ''' '''
    self.scraper.get_soup()
    
    titles_parent = self.scraper.soup.find_all('p',find_config)
    
    #The text for each title we take the text and clean it up with strip 
    self.titles = [title.text.strip() for title in titles_parent]
    return self.titles

  def get_paper_authors(self,find_config = {'class':'authors'}):  
    #setup the author search
    self.scraper.get_soup()
    self.author_names = []
    authors_parent = self.scraper.soup.find_all('p',find_config)
    
    #the titles and the papers Note: This code is subject to change since the website could change at anytime.
    for authors in authors_parent:
      name_group = authors.find_all('a')
      self.author_names = [name.text for name in name_group]
      
   
    return self.author_names

  
  def get_paper_tags(self,find_config = {'class':'tags is-inline-block'}):  
    self.scraper.get_soup()

    self.paper_tags = []
    tag_parents = self.scraper.soup.find_all('div',{'class':'tags is-inline-block'})
    
    for i in tag_parents:
      paper_tag = [j['data-tooltip'] for j in i.find_all('span')]
      self.paper_tags.append(paper_tag)
    return self.paper_tags

  def get_paper_doi(self,find_config = {'class':'list-title is-inline-block'}):
    
    self.scraper.get_soup()
    self.paper_doi = []

    doi_parents = self.scraper.soup.find_all('p',find_config)
    self.paper_doi = [doi.find('a')['href'] for doi in doi_parents]

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


