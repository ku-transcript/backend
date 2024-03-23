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
		courses := data.ReadCourses("data")

		return c.JSON(courses)
	})

	app.Post("/api/transcript/validate", func(c *fiber.Ctx) error {
		var request parser.Student
		if err := c.BodyParser(&request); err != nil {
			return err
		}

		if strings.Compare(request.StudentMajor, "Computer Science") == 0 {
			return c.JSON(validator.CS60Validator(request))
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

			if err != nil {
				return c.Status(fiber.StatusBadRequest).JSON(map[string]interface{}{
					"error": "Invalid transcript.",
				})
			}

			// Delete the files from disk
			if err := os.Remove(file.Filename); err != nil {
				return err
			}
		}

		return c.JSON(student)
	})
}
