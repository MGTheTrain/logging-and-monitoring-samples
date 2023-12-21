using HelloWorldService.Infrastructure.Settings;

var builder = WebApplication.CreateBuilder(args);

builder.Services.Configure<LokiConfigSettings>(builder.Configuration.GetSection("LokiConfigSettings"));
builder.Services.AddControllers();

var app = builder.Build();

app.UseRouting();
app.UseAuthorization();
app.MapControllers();
app.Run();
