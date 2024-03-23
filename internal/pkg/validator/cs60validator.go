package validator

import (
	"ku-transcript/internal/pkg/calculator"
	"ku-transcript/internal/pkg/utils/data"
	"ku-transcript/internal/pkg/utils/parser"
	"regexp"
)

func CS60Validator(student parser.Student) map[string]interface{} {
	requiredCredits := map[string]int{
		"วิชาแกน":                 16,
		"วิชาเฉพาะบังคับ":         55,
		"วิชาเฉพาะเลือก":          21,
		"ภาษากับการสื่อสาร":       13,
		"พลเมืองไทยและพลเมืองโลก": 3,
		"ศาสตร์แห่งผู้ประกอบการ":  3,
		"สุนทรียศาสตร์":           3,
		"อยู่ดีมีสุข":             3,
		"คณะวิทยาศาสตร์":          5,
	}
	minSumCredit := 128

	totalCredits, total := calculator.CalculateTotalCredits(data.ReadCourses("data"), student.EnrolledCourses, requiredCredits)
	isGraduated := true

	// Check if student has enough credits for each category
	for key, value := range totalCredits {
		if value < requiredCredits[key] {
			isGraduated = false
			break
		}
	}

	// Check if student enrolled in required courses
	pe := 0
	eng := 0
	thai := 0
	knowledgeOfTheLand := 0
	digital := 0

	peRegex := regexp.MustCompile(`01175\d{3}`)
	engRegex := regexp.MustCompile(`01355\d{3}`)
	thaiRegex := regexp.MustCompile(`01361101|01361102|01361103|01999021|01999022|02701011`)
	knowledgeOfTheLandRegex := regexp.MustCompile(`01999111`)
	digitalRegex := regexp.MustCompile(`01418131|01420245|01420246`)

	for _, course := range student.EnrolledCourses {
		courseID := course.CourseID

		if m := peRegex.MatchString(courseID); m {
			pe += 1
		}

		if m := engRegex.MatchString(courseID); m {
			eng += 1
		}

		if m := thaiRegex.MatchString(courseID); m {
			thai += 1
		}

		if m := knowledgeOfTheLandRegex.MatchString(courseID); m {
			knowledgeOfTheLand += 1
		}

		if m := digitalRegex.MatchString(courseID); m {
			digital += 1
		}
	}

	if pe < 1 || eng < 3 || thai < 1 || knowledgeOfTheLand < 1 || digital < 1 {
		isGraduated = false
	}

	// Check if student has enough total credits
	if total < minSumCredit {
		isGraduated = false
	}

	// Check cumulative GPA
	if student.StudentCumGPA < 2.00 {
		isGraduated = false
	}

	return map[string]interface{}{
		"total_credits": totalCredits,
		"total":         total,
		"is_graduated":  isGraduated,
	}
}
