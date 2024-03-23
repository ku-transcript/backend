# From: https://docs.docker.com/language/golang/build-images/#multi-stage-builds

# Build the application from source
FROM golang:1.22.1 AS build-stage

WORKDIR /app

COPY go.mod go.sum ./
RUN go mod download

COPY . .

RUN go build -o ku-transcript-backend cmd/main.go

# Run the tests in the container
FROM build-stage AS run-test-stage
RUN go test -v ./...

# Deploy the application binary into a lean image
FROM ubuntu:22.04 AS build-release-stage

WORKDIR /

RUN apt-get update && apt-get install -y poppler-utils

COPY --from=build-stage /app/ku-transcript-backend /ku-transcript-backend

EXPOSE 3000

CMD ["/ku-transcript-backend"]