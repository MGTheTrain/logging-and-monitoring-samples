using Prometheus;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllers();

var app = builder.Build();

// app.UseHttpsRedirection();

app.UseRouting();

// app.UseMetricServer(9102); // Challenges were faced in the Windows OS test system. It's advisable to allocate a distinct port for Prometheus to gather metrics. This should work on Unix systems (Linux debian or Linux Ubuntu and Mac OS versions). Consider updating the ../../../../prometheus/prometheus.yml configuration accordingly
app.UseMetricServer();
app.UseHttpMetrics();

app.UseAuthorization();

app.MapControllers();

app.Run();
