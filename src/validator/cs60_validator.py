import re

class CS60Validator:
  
  required_credit = {
    'วิชาแกน': 16, 
    'วิชาเฉพาะบังคับ': 55, 
    'วิชาเฉพาะเลือก': 21, 
    'ภาษากับการสื่อสาร': 13, 
    'พลเมืองไทยและพลเมืองโลก': 3, 
    'ศาสตร์แห่งผู้ประกอบการ': 3, 
    'สุนทรียศาสตร์': 3, 
    'อยู่ดีมีสุข': 3,
    'คณะวิทยาศาสตร์': 5,
  }
  
  def validate(self, student_data):
    # check credit
    course_categories = self.required_credit.keys()
    total_credit = student_data["total_credit_per_category"]
    
    for course_category in course_categories:
      if total_credit[course_category] < self.required_credit[course_category]:
        return False
      
    # check required course (e.g. P.E, Eng)
    enrolled_courses = student_data["enrolled_courses"]
    
    pe = 0
    eng = 0
    thai = 0
    knowledge_of_the_land = 0
    digital = 0
    science = 0
    
    for enrolled_course in enrolled_courses:
      course_id = enrolled_course["course_id"]
      
      # pe
      if re.search("01175\d{3}", course_id):
        pe += 1
            
      # eng
      if re.search("01355\d{3}", course_id):
        eng += 1
      
      # thai
      if re.search("01361101|01361102|01361103|01999021|01999022|02701011", course_id):
        thai += 1
      
      # knowledge of the land
      if re.search("01999111", course_id):
        knowledge_of_the_land += 1
      
      # digital
      if re.search("01418131|01420245|01420246", course_id):
        digital += 1
            
    if pe < 1 or eng < 3 or thai < 1 or knowledge_of_the_land < 1 or digital < 1:
      return False
    
    if sum([total_credit[c] for c in ['วิชาแกน', 'วิชาเฉพาะบังคับ', 'วิชาเฉพาะเลือก', 'ภาษากับการสื่อสาร', 'พลเมืองไทยและพลเมืองโลก', 'ศาสตร์แห่งผู้ประกอบการ']])
      
    # check grade
    if student_data["student_cum_gpa"] < 2:
      return False
      
    return True