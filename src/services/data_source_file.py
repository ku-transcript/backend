import json
from os import listdir
from os.path import isfile, join

class DataSourceFile:
  
  '''
  Read data from json file
  
  @return list of courses
  '''
  def fetch(self):
    # path contain files of courses
    path = "data"
    files = [f for f in listdir(path) if isfile(join(path, f))]
    data = []
    
    for file in files:
      data.extend(json.load(open(join(path, file))))
        
    return data