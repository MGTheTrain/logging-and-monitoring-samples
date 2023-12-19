package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
	"github.com/prometheus/client_golang/prometheus/promhttp"
)

func main() {
	router := gin.Default()

	// Hello World endpoint
	router.GET("/api/v1/hws", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"message": "Hello World from Go",
		})
	})

	// Metrics endpoint for Prometheus
	router.GET("/metrics", gin.WrapH(promhttp.Handler()))

	// Start the server on port 80
	if err := router.Run(":80"); err != nil {
		panic(err)
	}
}
