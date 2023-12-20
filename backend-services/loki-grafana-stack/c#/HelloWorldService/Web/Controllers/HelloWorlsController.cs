using Microsoft.AspNetCore.Mvc;

namespace HelloWorldService.Web.Controllers;

[Route("api/v1/hws")]
public class HelloWorldController : ControllerBase
{
    private static readonly NLog.Logger Logger = NLog.LogManager.GetCurrentClassLogger();
    public HelloWorldController(){}   

    /// <summary>
    /// Hello world reponse endpoint 
    /// </summary>
    /// <response code="200">If operation succeeded</response>
    /// <return>Returns awaitable task</return>
    [HttpGet]
    [Produces("application/json")]
    public async Task<IActionResult> GetUploadBlobsMetainformation()
    {
        var jsonMessage = "{\"message\": \"Hello from C# ASP .NET Core\"}";
        Logger.Info(jsonMessage);
        return await Task.FromResult(StatusCode(200, jsonMessage));
    }
}
