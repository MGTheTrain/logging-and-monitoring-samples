using Prometheus;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllers();

var app = builder.Build();

// app.UseHttpsRedirection();

app.UseRouting();

app.UseMetricServer(9102);
app.UseHttpMetrics();

app.UseAuthorization();

app.MapControllers();

app.Run();
