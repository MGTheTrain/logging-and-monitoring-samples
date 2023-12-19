FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /app
COPY . .
RUN dotnet restore HelloWorldService.csproj
RUN dotnet publish HelloWorldService.csproj -c Release -o out

FROM mcr.microsoft.com/dotnet/aspnet:6.0-alpine
WORKDIR /app
COPY --from=build /app/out .
EXPOSE 80
EXPOSE 9102
ENTRYPOINT ["dotnet", "HelloWorldService.dll"]

# building the docker image from `cd ../..`: sudo docker build -t hello-world-service:0.1.0 -f src/HelloWorldService/Dockerfile .
# run a docker container: sudo docker run --rm -p 5001:80 -d hello-world-service:0.1.0 