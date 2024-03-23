package main

import (
	"ku-transcript/internal/app/controllers"

	"github.com/gofiber/fiber/v2"
)

func main() {

	app := fiber.New()

	controllers.Init(app)

	app.Listen(":3000")
}
