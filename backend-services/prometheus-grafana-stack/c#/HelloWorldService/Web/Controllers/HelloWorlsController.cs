using Microsoft.AspNetCore.Mvc;

namespace HelloWorldService.Web.Controllers;

[Route("api/v1/hws")]
public class HelloWorldController : ControllerBase
{
    public HelloWorldController(ILogger<HelloWorldController> logger){}

    /// <summary>
    /// Hello world reponse endpoint 
    /// </summary>
    /// <response code="200">If operation succeeded</response>
    /// <return>Returns awaitable task</return>
    [HttpGet]
    [Produces("application/json")]
    public async Task<IActionResult> Hello()
    {
        var jsonMessage = "{\"message\": \"Hello from C# ASP .NET Core\"}";
        return await Task.FromResult(StatusCode(200, jsonMessage));
    }
}
