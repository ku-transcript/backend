from validate_data import validate
from calculate_total_credit import calculate
from data_source_file import DataSourceFile
# Quickly import file from another folder (NOT GOOD!)
import sys
sys.path.append("src/validator")
from cs60_validator import CS60Validator

def check_graduation(student_data):
  student_id = student_data["student_id"]
  years = int(student_id[0:2])
  
  total_credit = calculate(student_data["enrolled_courses"], DataSourceFile())
  
  result = None
  
  # (FUTURE) Add more if-else for different major and years
  if student_data["student_major"] == "Computer Science" and years >= 60 and years < 65:
    result = validate(student_data, total_credit, CS60Validator())
  
  # Currently except only CS Major (TODO: throw error)
  
  student_data.update({
    "is_graduate": result,
    "total_credit_per_category": total_credit
  })
  
  return student_data