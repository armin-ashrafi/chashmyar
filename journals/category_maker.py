#We make the query dictionary


#we first create a list of all the important services, and then list their important related queries.
#this will be a dictionary of sets.

categories = ['amd','cmd','retinoblastoma prediction','fundus multi disease','cornea ulcer','retinoblastoma semi clustering','cornea graft rejection','diabetic retinopathy','cataracts',
              'glaucoma','keratoconus','astigmatism','keratitis']
machine_learning_terms = ['computer vision','machine learning','deep learning','neural networks','convolutional neural networks','CNN','medical image','eye image','LSTM','Long-short term memory']
image_type_terms = ['fundus','slit','oct','topogoraphy','']
space = ' '

def query_maker(terms:list[list]) -> dict:
  queries = {}
  for cat in categories:
    queries[cat] = set()

#code for any number of lists
#search_term = ''
  #for term_list in terms:
    #for term in term_list:
      #search_term += term
      #break
  #code for exactly 3 lists
  for cat in categories:
    for ml_term in machine_learning_terms:
      for img_term in image_type_terms:
        search_term = cat + ' ' + ml_term + ' ' + img_term
        queries[cat].add(search_term)
  return queries
