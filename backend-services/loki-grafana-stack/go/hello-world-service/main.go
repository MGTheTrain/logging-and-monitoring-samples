package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func main() {
	router := gin.Default()

	// Hello World endpoint
	router.GET("/api/v1/hws", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"message": "Hello World from Go",
		})
	})

	// Start the server on port 80
	if err := router.Run(":80"); err != nil {
		panic(err)
	}
}
