FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build
WORKDIR /app
COPY . .
RUN dotnet restore ./backend-services/prometheus-grafana-stack/c#/HelloWorldService/HelloWorldService.csproj
RUN dotnet publish ./backend-services/prometheus-grafana-stack/c#/HelloWorldService/HelloWorldService.csproj -c Release -o out

FROM mcr.microsoft.com/dotnet/aspnet:7.0-alpine
WORKDIR /app
COPY --from=build /app/out .
EXPOSE 80
EXPOSE 9102
ENTRYPOINT ["dotnet", "HelloWorldService.dll"]

# building the docker image on Unix systems from `cd ../../../../`: sudo docker build -t csharp-hello-world-service:0.1.0 -f ./backend-services/prometheus-grafana-stack/c#/HelloWorldService/Dockerfile .
# run a docker container on Unix systems: sudo docker run --rm -p 5001:80 -d csharp-hello-world-service:0.1.0 