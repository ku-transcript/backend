package data

import (
	"encoding/json"
	"io"
	"log"
	"os"

	"ku-transcript/internal/pkg/utils/parser"
)

func ReadCourses() []parser.Course {

	files, err := os.ReadDir("data")
	if err != nil {
		log.Fatal(err)
	}

	var courses []parser.Course

	for _, file := range files {
		jsonFile, err := os.Open("data/" + file.Name())
		if err != nil {
			panic(err)
		}

		defer jsonFile.Close()

		byteValue, _ := io.ReadAll(jsonFile)

		var tmp []parser.Course
		json.Unmarshal(byteValue, &tmp)

		courses = append(courses, tmp...)
	}

	return courses
}
