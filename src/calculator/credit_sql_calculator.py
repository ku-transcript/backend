import db

'''
This class use SQL select query to sum up the total credit
'''
class CreditSQLCalculator:
  
    ignore_grades = ["P", "F", "W"]

    query = '''
          SELECT course_category, SUM(course_credit) AS total_credit 
          FROM (
            SELECT course_id, course_category, course_credit 
            FROM courses
            UNION ALL
            SELECT course_id, course_faculty AS course_category, course_credit 
            FROM courses 
            WHERE course_faculty NOT NULL
            )  
          WHERE course_id IN (%s)
          GROUP BY course_category
          '''

    def calculate_total_credit(self, enrolled_courses):

        conn = db.get_db_connection()
        cur = conn.cursor()

        enrolled_course_ids = [course['course_id'] for course in enrolled_courses if course['student_grade'] not in self.ignore_grades]

        # Select data from the table
        res = cur.execute(self.query % ','.join('?'*len(enrolled_course_ids)), enrolled_course_ids)

        data = res.fetchall()
        conn.close()

        d = dict()

        for r in data: 
            result = dict(r)
            d[result['course_category']] = result['total_credit']

        print(d)

        return d