import json

class FileData:
  
  '''
  Read data from json file
  
  @return list of courses
  '''
  def fetch(self):
    file1 = open("data/ku_ge.json")
    file2 = open("data/ku_cs60.json")
    
    data1 = json.load(file1) # list of gened courses
    data2 = json.load(file2) # list of cs courses
    
    data1.extend(data2) # merge two lists
        
    return data1
  

# f = FileData()

# data = f.fetch()

# print(data)