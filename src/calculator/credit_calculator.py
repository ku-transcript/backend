'''
Normal credit calculator sum by using for-loop
'''
class CreditCalculator:
  
    ignore_grades = ["P", "F", "W"]

    def __init__(self, data_source):
        self.courses = data_source.fetch()

    def calculate_total_credit(enrolled_courses):

        total_credit = {}
        ignore_grades = ["P", "F", "W"]

        for enrolled_course in enrolled_courses:
            for course in self.courses:

                if course["course_id"] != enrolled_course["course_id"] or enrolled_course["student_grade"] in ignore_grades:
                    continue

                if course["course_category"] not in total_credit:
                    total_credit[course["course_category"]] = course["course_credit"]
                else:
                    total_credit[course["course_category"]] += course["course_credit"]

                if "course_faculty" in course:
                    if course["course_faculty"] not in total_credit:
                        total_credit[course["course_faculty"]] = course["course_credit"]
                    else:
                        total_credit[course["course_faculty"]] += course["course_credit"]

        return total_credit
    