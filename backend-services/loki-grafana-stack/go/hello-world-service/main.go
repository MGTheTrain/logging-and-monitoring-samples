package main

import (
	"fmt"
	"log"
	"net/http"
	"time"

	"github.com/afiskon/promtail-client/promtail"
	"github.com/gin-gonic/gin"
	"github.com/spf13/viper"
)

var loki promtail.Client // Change the variable declaration

func initLokiClient(url string) {
	sourceName := "hello-world-service"
	jobName := "hello-world-service-job"

	labels := "{source=\"" + sourceName + "\",job=\"" + jobName + "\"}"
	conf := promtail.ClientConfig{
		PushURL:            url,
		Labels:             labels,
		BatchWait:          5 * time.Second,
		BatchEntriesNumber: 10000,
		SendLevel:          promtail.INFO,
		PrintLevel:         promtail.ERROR,
	}

	var err error
	loki, err = promtail.NewClientProto(conf) // Update this line
	if err != nil {
		log.Printf("promtail.NewClient: %s\n", err)
	}
}

func logToLoki(message string) {
	timestamp := time.Now().String()
	loki.Infof("source = hello-world-service, time = %s, message = %s\n", timestamp, message)
}

func loadConfiguration() string {
	// Load configuration from file
	viper.SetConfigName("appsettings") // Config file name without extension
	viper.SetConfigType("yaml")        // Config file type (yaml, json, etc.)
	viper.AddConfigPath(".")           // Path to look for the config file (current directory)
	// Disable environment variable prefixing
	viper.SetEnvPrefix("") // Empty string indicates no prefix
	viper.AutomaticEnv()   // Allow Viper to read environment variables directly without a prefix

	// Read in the config file
	if err := viper.ReadInConfig(); err != nil {
		fmt.Printf("Error reading config file: %s. Attempting to access environment variables", err)
	}

	// Retrieve the URL from the configuration
	url := viper.GetString("loki.url")
	// e.g. "http://192.168.99.100:3100/api/prom/push"
	if url == "" {
		url = viper.GetString("LOKI_URL")
	}
	if url == "" {
		panic("Loki URL is not set")
	}
	return url
}

func main() {
	var url = loadConfiguration()
	initLokiClient(url)

	router := gin.Default()

	// Hello World endpoint
	router.GET("/api/v1/hws", func(c *gin.Context) {
		logToLoki("Hello World from Go")
		c.JSON(http.StatusOK, gin.H{
			"message": "Hello World from Go",
		})
	})

	// Start the server on port 80
	if err := router.Run(":80"); err != nil {
		panic(err)
	}
}
