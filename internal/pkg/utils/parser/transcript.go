package parser

import (
	"errors"
	"regexp"
	"strconv"
	"strings"
)

const (
	transcriptPattern = `KASETSART UNIVERSITY`
	coursePattern     = `\s*(\d{8})\s*(.+)\s*([A-D][+]?|[FPNW])\s*(\d)`
	pattern1          = `Student No\s*(\d{10})\s*Faculty Of\s*(.+)`
	pattern2          = `Name\s*(Miss|Mr\.) (.+)\s*Field Of Study\s*(.+)`
	pattern3          = `Date Of Admission\s*(\w+ \d{1,2}, \d{4})`
	pattern4          = `(น[\p{L}\p{N}\p{M}_]+) ([\p{L}\p{N}\p{M}_]+ [\p{L}\p{N}\p{M}_]+)` // [\p{L}\p{N}\p{M}_]+ match any unicode
	pettern5          = `cum G.P.A. =\s*(\d+\.\d+)`
)

type Course struct {
	CourseID       string `json:"course_id"`
	CourseName     string `json:"course_name"`
	StudentGrade   string `json:"student_grade"`
	CourseCredit   int    `json:"course_credit"`
	CourseCategory string `json:"course_category"`
	CourseFaculty  string `json:"course_faculty"`
}

type Student struct {
	StudentId       string   `json:"student_id"`
	StudentFaculty  string   `json:"student_faculty"`
	StudentENTitle  string   `json:"student_en_title"`
	StudentENName   string   `json:"student_en_name"`
	StudentTHTitle  string   `json:"student_th_title"`
	StudentTHName   string   `json:"student_th_name"`
	StudentMajor    string   `json:"student_major"`
	StudentCumGPA   float64  `json:"student_cum_gpa"`
	DateOfAdmission string   `json:"date_of_admission"`
	EnrolledCourses []Course `json:"enrolled_courses"`
}

func ParseText(text string) (Student, error) {

	r, _ := regexp.Compile(coursePattern)
	r1, _ := regexp.Compile(pattern1)
	r2, _ := regexp.Compile(pattern2)
	r3, _ := regexp.Compile(pattern3)
	r4, _ := regexp.Compile(pattern4)
	r5, _ := regexp.Compile(pettern5)
	r6, _ := regexp.Compile(transcriptPattern)

	transcriptMatch := r6.FindString(text)

	if transcriptMatch == "" {
		return Student{}, errors.New("INVALID TRANSCRIPT")
	}

	matches := r.FindAllStringSubmatch(text, -1)
	matche1 := r1.FindStringSubmatch(text)
	matche2 := r2.FindStringSubmatch(text)
	matche3 := r3.FindStringSubmatch(text)
	matche4 := r4.FindStringSubmatch(text)
	matche5 := r5.FindAllStringSubmatch(text, -1)

	enrolledCourses := make([]Course, 0)

	for _, match := range matches {
		courseCredit, err := strconv.Atoi(strings.TrimSpace(match[4]))
		if err != nil {
			courseCredit = 0
		}
		enrolledCourses = append(enrolledCourses, Course{
			CourseID:     strings.TrimSpace(match[1]),
			CourseName:   strings.TrimSpace(match[2]),
			StudentGrade: strings.TrimSpace(match[3]),
			CourseCredit: courseCredit,
		})
	}

	studentCumGPA, err := strconv.ParseFloat(strings.TrimSpace(matche5[len(matche5)-1][1]), 64)

	if err != nil {
		studentCumGPA = 0
	}

	return Student{
		StudentId:       strings.TrimSpace(matche1[1]),
		StudentFaculty:  strings.TrimSpace(matche1[2]),
		StudentENTitle:  strings.TrimSpace(matche2[1]),
		StudentENName:   strings.TrimSpace(matche2[2]),
		StudentTHTitle:  strings.TrimSpace(matche4[1]),
		StudentTHName:   strings.TrimSpace(matche4[2]),
		StudentMajor:    strings.TrimSpace(matche2[3]),
		DateOfAdmission: strings.TrimSpace(matche3[1]),
		StudentCumGPA:   studentCumGPA,
		EnrolledCourses: enrolledCourses,
	}, nil
}
