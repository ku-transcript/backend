package calculator

import (
	"encoding/json"
	"ku-transcript/internal/pkg/utils/data"
	"ku-transcript/internal/pkg/utils/parser"
	"testing"
)

func TestCalculateTotalCredit(t *testing.T) {

	enrolledCoursesJson := `
	[
		{
				"course_credit": 3,
				"course_id": "01355101",
				"course_name": "English for Everyday Life",
				"student_grade": "P"
		},
		{
				"course_credit": 3,
				"course_id": "01355102",
				"course_name": "English for University Life",
				"student_grade": "A"
		},
		{
				"course_credit": 3,
				"course_id": "01417111",
				"course_name": "Calculus I",
				"student_grade": "C"
		},
		{
				"course_credit": 3,
				"course_id": "01418112",
				"course_name": "Fundamental Programming Concepts",
				"student_grade": "B+"
		},
		{
				"course_credit": 2,
				"course_id": "01418114",
				"course_name": "Introduction to Computer Science",
				"student_grade": "B"
		},
		{
				"course_credit": 3,
				"course_id": "01418131",
				"course_name": "Digital Computer Logic",
				"student_grade": "A"
		},
		{
				"course_credit": 3,
				"course_id": "01999021",
				"course_name": "Thai Language for Communication",
				"student_grade": "A"
		},
		{
				"course_credit": 2,
				"course_id": "01999111",
				"course_name": "Knowledge of the Land",
				"student_grade": "A"
		},
		{
				"course_credit": 3,
				"course_id": "01101101",
				"course_name": "General Economics in Globalization",
				"student_grade": "A"
		},
		{
				"course_credit": 3,
				"course_id": "01355103",
				"course_name": "English for Job Opportunities",
				"student_grade": "A"
		},
		{
				"course_credit": 1,
				"course_id": "01371111",
				"course_name": "Information Media for Learning",
				"student_grade": "A"
		},
		{
				"course_credit": 3,
				"course_id": "01387102",
				"course_name": "Philosophy for New World",
				"student_grade": "A"
		},
		{
				"course_credit": 3,
				"course_id": "01417112",
				"course_name": "Calculus II",
				"student_grade": "C"
		},
		{
				"course_credit": 3,
				"course_id": "01418113",
				"course_name": "Computer Programming",
				"student_grade": "A"
		},
		{
				"course_credit": 4,
				"course_id": "01418132",
				"course_name": "Fundamentals of Computing",
				"student_grade": "B+"
		},
		{
				"course_credit": 1,
				"course_id": "02999144",
				"course_name": "Life Skills For Undergraduate Student",
				"student_grade": "A"
		},
		{
				"course_credit": 1,
				"course_id": "01175161",
				"course_name": "Brain Training with Playing Bridge",
				"student_grade": "A"
		},
		{
				"course_credit": 3,
				"course_id": "01417322",
				"course_name": "Basic Linear Algebra",
				"student_grade": "B+"
		},
		{
				"course_credit": 3,
				"course_id": "01418102",
				"course_name": "Information Technology for Entrepreneurs",
				"student_grade": "A"
		},
		{
				"course_credit": 3,
				"course_id": "01418211",
				"course_name": "Software Construction",
				"student_grade": "A"
		},
		{
				"course_credit": 3,
				"course_id": "01418231",
				"course_name": "Data Structures",
				"student_grade": "B"
		},
		{
				"course_credit": 2,
				"course_id": "01421201",
				"course_name": "Radiation, Life and Environment",
				"student_grade": "A"
		},
		{
				"course_credit": 3,
				"course_id": "01422111",
				"course_name": "Principles of Statistics",
				"student_grade": "C+"
		},
		{
				"course_credit": 3,
				"course_id": "01387103",
				"course_name": "Philosophy of Sufficiency Economics and Buddhism",
				"student_grade": "A"
		},
		{
				"course_credit": 3,
				"course_id": "01401201",
				"course_name": "Plants for Value of Life Creation",
				"student_grade": "A"
		},
		{
				"course_credit": 3,
				"course_id": "01418221",
				"course_name": "Fundamentals of Database Systems",
				"student_grade": "B+"
		},
		{
				"course_credit": 3,
				"course_id": "01418232",
				"course_name": "Algorithm Design and Analysis",
				"student_grade": "B"
		},
		{
				"course_credit": 4,
				"course_id": "01418233",
				"course_name": "Assembly Language and Computer Architecture",
				"student_grade": "B+"
		},
		{
				"course_credit": 3,
				"course_id": "01418241",
				"course_name": "Financial and Bangking Information Technology",
				"student_grade": "A"
		},
		{
				"course_credit": 3,
				"course_id": "01999033",
				"course_name": "Arts of Living",
				"student_grade": "A"
		},
		{
				"course_credit": 3,
				"course_id": "01418321",
				"course_name": "System Analysis and Design",
				"student_grade": "A"
		},
		{
				"course_credit": 4,
				"course_id": "01418331",
				"course_name": "Operating Systems",
				"student_grade": "B+"
		},
		{
				"course_credit": 3,
				"course_id": "01418341",
				"course_name": "Intellectual Properties and Professional Ethics",
				"student_grade": "A"
		},
		{
				"course_credit": 3,
				"course_id": "01418342",
				"course_name": "Enterprise Resource Planning System Design and Develop",
				"student_grade": "A"
		},
		{
				"course_credit": 3,
				"course_id": "01418442",
				"course_name": "Web Technology and Web Services",
				"student_grade": "W"
		},
		{
				"course_credit": 3,
				"course_id": "01418471",
				"course_name": "Introduction to Software Engineering",
				"student_grade": "A"
		},
		{
				"course_credit": 1,
				"course_id": "01418497",
				"course_name": "Seminar",
				"student_grade": "B+"
		},
		{
				"course_credit": 3,
				"course_id": "01355203",
				"course_name": "English Language Structure",
				"student_grade": "W"
		},
		{
				"course_credit": 3,
				"course_id": "01418332",
				"course_name": "Information System Security",
				"student_grade": "B+"
		},
		{
				"course_credit": 2,
				"course_id": "01418333",
				"course_name": "Automata Theory",
				"student_grade": "A"
		},
		{
				"course_credit": 2,
				"course_id": "01418334",
				"course_name": "Compiler Techniques",
				"student_grade": "B+"
		},
		{
				"course_credit": 3,
				"course_id": "01418344",
				"course_name": "Mobile Application Design and Development",
				"student_grade": "A"
		},
		{
				"course_credit": 3,
				"course_id": "01418351",
				"course_name": "Computer Communications and Cloud Computing Principles",
				"student_grade": "B+"
		},
		{
				"course_credit": 1,
				"course_id": "01418390",
				"course_name": "Cooperative Education Preparation",
				"student_grade": "A"
		},
		{
				"course_credit": 3,
				"course_id": "01418441",
				"course_name": "Business Data Dimension and Report Management",
				"student_grade": "B+"
		},
		{
				"course_credit": 6,
				"course_id": "01418490",
				"course_name": "Cooperative Education",
				"student_grade": "A"
		},
		{
				"course_credit": 3,
				"course_id": "01418472",
				"course_name": "PM",
				"student_grade": "A"
		},
		{
				"course_credit": 3,
				"course_id": "01355203",
				"course_name": "Eng",
				"student_grade": "B+"
		},
		{
				"course_credit": 3,
				"course_id": "01418499",
				"course_name": "Project",
				"student_grade": "A"
		}
]
	`
	expectedTotalCredits := map[string]int{
		"คณะมนุษยศาสตร์":                   0,
		"คณะวิทยาศาสตร์":                   6,
		"คณะศึกษาศาสตร์":                   0,
		"คณะเศรษฐศาสตร์":                   0,
		"พลเมืองไทยและพลเมืองโลก":          3,
		"ภาษากับการสื่อสาร":                13,
		"วิชาเฉพาะบังคับ":                  55,
		"วิชาเฉพาะเลือก":                   21,
		"วิชาเสรี":                         6,
		"วิชาแกน":                          16,
		"วิทยาลัยบูรณาการศาสตร์":           0,
		"ศาสตร์แห่งผู้ประกอบการ":           3,
		"สุนทรียศาสตร์":                    3,
		"อยู่ดีมีสุข":                      3,
		"โครงการบูรณาการ วิทยาเขตกำแพงแสน": 0,
	}

	var enrolledCourses []parser.Course

	if err := json.Unmarshal([]byte(enrolledCoursesJson), &enrolledCourses); err != nil {
		t.Error(err)
	}

	totalCredits, total := CalculateTotalCredits(data.ReadCourses("../../../data"), enrolledCourses, map[string]int{
		"วิชาแกน":                 16,
		"วิชาเฉพาะบังคับ":         55,
		"วิชาเฉพาะเลือก":          21,
		"ภาษากับการสื่อสาร":       13,
		"พลเมืองไทยและพลเมืองโลก": 3,
		"ศาสตร์แห่งผู้ประกอบการ":  3,
		"สุนทรียศาสตร์":           3,
		"อยู่ดีมีสุข":             3,
		"คณะวิทยาศาสตร์":          5,
	})

	if total != 129 {
		t.Errorf("Expected total to be 128, got %d", total)
	}

	for key, value := range totalCredits {
		if value != expectedTotalCredits[key] {
			t.Errorf("Expected %s to have %d credits, got %d", key, expectedTotalCredits[key], value)
		}
	}
}
