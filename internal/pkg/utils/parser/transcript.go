package parser

import (
	"regexp"
	"strings"
)

const (
	coursePattern = `\s*(\d{8})\s*(.+)\s*([A-D][+]?|[FPNW])\s*(\d)`
	pattern1      = `Student No\s*(\d{10})\s*Faculty Of\s*(.+)`
	pattern2      = `Name\s*(Miss|Mr\.) (.+)\s*Field Of Study\s*(.+)`
	pattern3      = `Date Of Admission\s*(\w+ \d{1,2}, \d{4})`
	pattern4      = `(น[\p{L}\p{N}\p{M}_]+) ([\p{L}\p{N}\p{M}_]+ [\p{L}\p{N}\p{M}_]+)` // [\p{L}\p{N}\p{M}_]+ match any unicode
)

type Course struct {
	CourseID     string `json:"course_id"`
	CourseName   string `json:"course_name"`
	StudentGrade string `json:"student_grade"`
	CourseCredit string `json:"course_credit"`
}

type Student struct {
	StudentId       string   `json:"student_id"`
	StudentFaculty  string   `json:"student_faculty"`
	StudentENTitle  string   `json:"student_en_title"`
	StudentENName   string   `json:"student_en_name"`
	StudentTHTitle  string   `json:"student_th_title"`
	StudentTHName   string   `json:"student_th_name"`
	StudentMajor    string   `json:"student_major"`
	DateOfAdmission string   `json:"date_of_admission"`
	EnrolledCourses []Course `json:"enrolled_courses"`
}

func ParseText(text string) Student {

	r, _ := regexp.Compile(coursePattern)
	r1, _ := regexp.Compile(pattern1)
	r2, _ := regexp.Compile(pattern2)
	r3, _ := regexp.Compile(pattern3)
	r4, _ := regexp.Compile(pattern4)

	matches := r.FindAllStringSubmatch(text, -1)
	matche1 := r1.FindStringSubmatch(text)
	matche2 := r2.FindStringSubmatch(text)
	matche3 := r3.FindStringSubmatch(text)
	matche4 := r4.FindStringSubmatch(text)

	// fmt.Println("Student No:", matche1[1])
	// fmt.Println("Faculty Of:", matche1[2])
	// fmt.Println("English Title:", matche2[1])
	// fmt.Println("English Name:", matche2[2])
	// fmt.Println("Field Of Study:", matche2[2])
	// fmt.Println("Date of Admission:", matche3[1])
	// fmt.Println("Thai Title:", matche4[1])
	// fmt.Println("Thai Name:", matche4[2])

	enrolledCourses := make([]Course, 0)

	for _, match := range matches {
		enrolledCourses = append(enrolledCourses, Course{
			CourseID:     match[1],
			CourseName:   strings.TrimSpace(match[2]),
			StudentGrade: match[3],
			CourseCredit: match[4],
		})
	}

	return Student{
		StudentId:       matche1[1],
		StudentFaculty:  matche1[2],
		StudentENTitle:  matche2[1],
		StudentENName:   matche2[2],
		StudentTHTitle:  matche4[1],
		StudentTHName:   matche4[2],
		StudentMajor:    matche2[3],
		DateOfAdmission: matche3[1],
		EnrolledCourses: enrolledCourses,
	}
}
