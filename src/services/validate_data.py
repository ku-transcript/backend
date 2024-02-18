'''
Validate if the student is graduated or not using the validator

@param {student_data} student data to validate
@param {validator} validator to check graduation for different major

@return True if graduate otherwise False
'''
def validate(student_data, total_credit, validator):
  return validator.validate(student_data, total_credit)
