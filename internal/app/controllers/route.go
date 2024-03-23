package controllers

import (
	"ku-transcript/internal/app/controllers/transcript"

	"github.com/gofiber/fiber/v2"
)

func Init(app *fiber.App) {
	app.Get("/", func(c *fiber.Ctx) error {
		return c.SendString("Hello, World!")
	})

	app.Get("/health", func(c *fiber.Ctx) error {
		return c.SendString("OK")
	})

	app.Get("/api/curriculum", transcript.GetCourses)

	app.Post("/api/transcript/validate", transcript.Validate)

	app.Post("/api/transcript/upload", transcript.Upload)
}
