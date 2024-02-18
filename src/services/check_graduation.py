from validate_data import validate
# Quickly import file from another folder (NOT GOOD!)
import sys
sys.path.append("src/validator")
from cs60_validator import CS60Validator

def check_graduation(student_data):
  student_id = student_data["student_id"]
  years = int(student_id[0:2])
    
  result = None
  
  # (FUTURE) Add more if-else for different major and years
  if student_data["student_major"] == "Computer Science" and years >= 60 and years < 65:
    result = validate(student_data, CS60Validator())
  
  # Currently except only CS Major (TODO: throw error)
  
  student_data.update({
    "is_graduate": result,
  })
  
  return student_data