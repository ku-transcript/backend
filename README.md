# KU Transcript Backend

## Usage

Upload your transcript by making a POST request to this endpoint with a form-data key `transcript` and value as the transcript file.

```
/api/transcript/upload
```

Response will be a JSON with student data from the transcript.

## Run with Docker

Build the image
```sh
docker build -t ku-transcript-backend .
```

Run the container
```sh
docker run --name ku-transcript-backend -p 3000:3000 ku-transcript-backend
```

## Run without Docker

Build go binary
```sh
go build -o ku-transcript-backend cmd/main.go
```

Run the binary
```sh
./ku-transcript-backend
```

## Generate Swagger Documentation

refer to [gofiber/swagger](https://github.com/gofiber/swagger?tab=readme-ov-files) for more information.

```sh
swag init --parseDependency -g ../../../cmd/main.go -d internal/app/controllers/
```

Go to `localhost:3000/swagger` to view the documentation.