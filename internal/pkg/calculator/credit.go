package calculator

import (
	"ku-transcript/internal/pkg/utils/parser"
)

func CalculateTotalCredits(courses []parser.Course, enrolled_courses []parser.Course, required_credits map[string]int) (map[string]int, int) {

	totalCredits := make(map[string]int)
	total := 0

	for _, enrolledCourse := range enrolled_courses {
		for _, c := range courses {
			if enrolledCourse.CourseID != c.CourseID || enrolledCourse.StudentGrade == "W" || enrolledCourse.StudentGrade == "F" || enrolledCourse.StudentGrade == "P" {
				continue
			}

			if _, ok := totalCredits[c.CourseCategory]; !ok && c.CourseCategory != "" {
				totalCredits[c.CourseCategory] = 0
			}
			if _, ok := totalCredits[c.CourseFaculty]; !ok && c.CourseFaculty != "" {
				totalCredits[c.CourseFaculty] = 0
			}

			if c.CourseCategory != "" && totalCredits[c.CourseCategory] < required_credits[c.CourseCategory] {
				totalCredits[c.CourseCategory] += c.CourseCredit
			} else if c.CourseFaculty != "" && totalCredits[c.CourseFaculty] < required_credits[c.CourseFaculty] {
				totalCredits[c.CourseFaculty] += c.CourseCredit
			} else {
				totalCredits["วิชาเสรี"] += c.CourseCredit
			}
			total += c.CourseCredit
		}
	}

	return totalCredits, total
}
