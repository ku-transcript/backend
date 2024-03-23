package controllers

import (
	"fmt"
	"ku-transcript/internal/pkg/utils/parser"
	"ku-transcript/internal/pkg/utils/pdf"
	"os"

	"github.com/gofiber/fiber/v2"
)

func Init(app *fiber.App) {
	app.Get("/", func(c *fiber.Ctx) error {
		return c.SendString("Hello, World!")
	})

	app.Post("/api/transcript/upload", func(c *fiber.Ctx) error {
		var student parser.Student

		form, err := c.MultipartForm()
		if err != nil {
			return err
		}

		// Get all files from "documents" key
		files := form.File["documents"] // => []*multipart.FileHeader

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
