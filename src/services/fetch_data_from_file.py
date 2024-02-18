import json
from os import listdir
from os.path import isfile, join

class FileData:
  
  '''
  Read data from json file
  
  @return list of courses
  '''
  def fetch(self):
    # file1 = open("data/ku_all_ge.json")
    # file2 = open("data/ku_cs60.json")
    path = "data"
    files = [f for f in listdir(path) if isfile(join(path, f))]
    
    data = []
    
    for file in files:
      data.extend(json.load(open(path + "/" + file)))
    
#     data1 = json.load(file1) # list of gened courses
#     data2 = json.load(file2) # list of cs courses
    
    # data1.extend(data2) # merge two lists
        
    return data
  

# f = FileData()

# data = f.fetch()

# print(data)