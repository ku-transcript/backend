from validate_data import validate
# Quickly import file from another folder (NOT GOOD!)
import sys
sys.path.append("src/validator")
from cs60_validator import CS60Validator
from datetime import datetime

def check_graduation(student_data):
  date_of_admission = student_data['date_of_admission']
  years = datetime.date(date_of_admission).year
    
  result = None
  
  # (FUTURE) Add more if-else for different major and years
  if student_data["student_major"] == "Computer Science" and years >= 2017 and years < 2022:
    result = validate(student_data, CS60Validator())
  
  # Currently except only CS Major (TODO: throw error)
  
  student_data.update({
    "is_graduate": result,
  })
  
  return student_data