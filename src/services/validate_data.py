from calculate_total_credit import calculate
from fetch_data_from_file import FileData

def validate(student_data, validator):
  f = FileData()
  courses = f.fetch()
  total_credit = calculate(student_data, courses)
  
  return validator.validate(student_data, total_credit)


