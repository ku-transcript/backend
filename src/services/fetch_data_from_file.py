import json

class FileData:
  
  def fetch(self):
    file1 = open("data/ku_ge.json")
    file2 = open("data/ku_cs60.json")
    
    data1 = json.load(file1)
    data2 = json.load(file2)
    
    
    # print("Return data = ", data)
    
    return data
  

f = FileData()

f.fetch()