from calculate_total_credit import calculate
from fetch_data_from_file import FileData

'''
Validate if the student is graduated or not using the validator

@param {student_data} student data to validate
@param {validator} validator

'''
def validate(student_data, validator):
  f = FileData()
  courses = f.fetch()
  total_credit = calculate(student_data["enrolled_courses"], courses)
  
  return validator.validate(student_data, total_credit)
