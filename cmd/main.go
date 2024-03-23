package main

import (
	"fmt"
	"ku-transcript/internal/pkg/utils/parser"
	"ku-transcript/internal/pkg/utils/pdf"
)

func main() {
	text := pdf.ExtractText()
	student := parser.ParseText(text)

	fmt.Printf("%+v\n", student)
}
