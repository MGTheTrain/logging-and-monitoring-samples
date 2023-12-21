using HelloWorldService.Infrastructure.Settings;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Options;
using Serilog;
using Serilog.Sinks.Loki;
using System;
using System.Runtime.CompilerServices;

namespace HelloWorldService.Web.Controllers
{
    [Route("api/v1/hws")]
    public class HelloWorldController : ControllerBase
    {
        private static LokiConfigSettings _lokiConfigSettings;
        private static bool _isLoggerInitialized = false;

        public HelloWorldController(IOptions<LokiConfigSettings> lokiConfigSettings)
        {
            _lokiConfigSettings = lokiConfigSettings.Value;

            if (!_isLoggerInitialized)
            {
                var credentials = new NoAuthCredentials(_lokiConfigSettings.LokiUrl);

                Log.Logger = new LoggerConfiguration()
                    .MinimumLevel.Information()
                    .Enrich.FromLogContext()
                    .WriteTo.LokiHttp(credentials)
                    .CreateLogger();

                Log.Information($"{DateTime.UtcNow} Initializing logger in HelloWorldController using URL: {_lokiConfigSettings.LokiUrl}");

                _isLoggerInitialized = true;
            }
        }

        /// <summary>
        /// Hello world response endpoint 
        /// </summary>
        /// <response code="200">If operation succeeded</response>
        /// <return>Returns awaitable task</return>
        [HttpGet]
        [Produces("application/json")]
        public IActionResult GetUploadBlobsMetainformation()
        {
            var jsonMessage = "{\"message\": \"Hello from C# ASP .NET Core\"}";

            var dateTime = DateTime.UtcNow;
            var logMessage = $"{dateTime} Hello from C# ASP .NET Core";
            Log.Information(logMessage);

            return StatusCode(200, jsonMessage);
        }
    }
}
