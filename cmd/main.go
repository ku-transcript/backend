package main

import (
	"ku-transcript/internal/app/controllers"

	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/swagger"

	_ "ku-transcript/docs"
)

func main() {

	app := fiber.New()

	app.Get("/swagger/*", swagger.HandlerDefault)

	controllers.Init(app)

	app.Listen(":3000")
}
