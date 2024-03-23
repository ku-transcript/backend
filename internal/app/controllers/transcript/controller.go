package transcript

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

// Check Graduation
// @Summary Check Graduation
// @Description Validate the student's transcript and check if they are eligible for graduation.
// @Accept json
// @Param student body parser.Student true "Student data"
// @Tags transcript
// @Produce  json
// @Success 200 {array} parser.Student "Student data"
// @Failure 400 {object} map[string]interface{} "Major not supported."
// @Router /api/transcript/validate [post]
func Validate(c *fiber.Ctx) error {
	var request parser.Student
	if err := c.BodyParser(&request); err != nil {
		return err
	}

	if strings.Compare(request.StudentMajor, "Computer Science") == 0 {
		return c.JSON(validator.CS60Validator(request))
	}

	return c.JSON(map[string]interface{}{
		"error": "Major not supported.",
	})
}

// Upload Transcript
// @Summary Upload Transcript
// @Description Upload a transcript and get the parsed data.
// @Accept multipart/form-data
// @Param transcript formData file true "Transcript file"
// @Tags transcript
// @Produce  json
// @Success 200 {array} parser.Student "Student data"
// @Failure 400 {object} map[string]interface{} "Invalid file type."
// @Failure 400 {object} map[string]interface{} "Invalid transcript."
// @Router /api/transcript/upload [post]
func Upload(c *fiber.Ctx) error {
	var student parser.Student

	form, err := c.MultipartForm()
	if err != nil {
		return err
	}

	// Get all files from "documents" key
	files := form.File["transcript"] // => []*multipart.FileHeader

	for _, file := range files {
		fmt.Println(file.Filename, file.Size, file.Header["Content-Type"][0])

		if file.Header["Content-Type"][0] != "application/pdf" {
			return c.Status(fiber.StatusBadRequest).JSON(map[string]interface{}{
				"error": "Invalid file type.",
			})
		}

		// Save the files to disk
		if err := c.SaveFile(file, fmt.Sprintf("./%s", file.Filename)); err != nil {
			return err
		}

		text := pdf.ExtractText(file.Filename)
		student, err = parser.ParseText(text)

		// Delete the files from disk
		if err := os.Remove(file.Filename); err != nil {
			return err
		}

		if err != nil {
			return c.Status(fiber.StatusBadRequest).JSON(map[string]interface{}{
				"error": "Invalid transcript.",
			})
		}

	}

	return c.JSON(student)
}

// Curriculum API
// @Summary Get All Courses
// @Description Retrieves a list of all available courses.
// @Tags courses
// @Produce  json
// @Success 200 {array} []parser.Course "List of courses"
// @Router /api/curriculum [get]
func GetCourses(c *fiber.Ctx) error {
	return c.JSON(data.ReadCourses("data"))
}
