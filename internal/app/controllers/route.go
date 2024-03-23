package controllers

import (
	"fmt"
	"ku-transcript/internal/pkg/utils/data"
	"ku-transcript/internal/pkg/utils/parser"
	"ku-transcript/internal/pkg/utils/pdf"
	"ku-transcript/internal/pkg/validator"
	"os"
	"strings"

	"github.com/gofiber/fiber/v2"
)

func Init(app *fiber.App) {
	app.Get("/", func(c *fiber.Ctx) error {
		return c.SendString("Hello, World!")
	})

	app.Get("/api/curriculum", func(c *fiber.Ctx) error {
		courses := data.ReadCourses()

		return c.JSON(courses)
	})

	app.Post("/api/transcript/validate", func(c *fiber.Ctx) error {
		type Request struct {
			EnrolledCourses []parser.Course `json:"enrolled_courses"`
			StudentCumGPA   float64         `json:"student_cum_gpa"`
			StudentMajor    string          `json:"student_major"`
			DateOfAdmission string          `json:"date_of_admission"`
		}

		var request Request

		if err := c.BodyParser(&request); err != nil {
			return err
		}

		if strings.Compare(request.StudentMajor, "Computer Science") == 0 {
			isGraduated, totalCredits, total := validator.CS60Validator(parser.Student{
				EnrolledCourses: request.EnrolledCourses,
				StudentCumGPA:   request.StudentCumGPA,
				StudentMajor:    request.StudentMajor,
				DateOfAdmission: request.DateOfAdmission,
			})

			response := map[string]interface{}{
				"total_credits": totalCredits,
				"total":         total,
				"is_graduated":  isGraduated,
			}

			return c.JSON(response)
		}

		return c.JSON(map[string]interface{}{
			"error": "Faculty not supported.",
		})
	})

	app.Post("/api/transcript/upload", func(c *fiber.Ctx) error {
		var student parser.Student

		form, err := c.MultipartForm()
		if err != nil {
			return err
		}

		// Get all files from "documents" key
		files := form.File["transcript"] // => []*multipart.FileHeader

		for _, file := range files {
			fmt.Println(file.Filename, file.Size, file.Header["Content-Type"][0])

			// Save the files to disk
			if err := c.SaveFile(file, fmt.Sprintf("./%s", file.Filename)); err != nil {
				return err
			}

			text := pdf.ExtractText(file.Filename)
			student = parser.ParseText(text)

			// Delete the files from disk
			if err := os.Remove(file.Filename); err != nil {
				return err
			}
		}

		return c.JSON(student)
	})
}
