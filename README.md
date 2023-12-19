# logging-and-monitoring-samples

## Table of Contents

- [Summary](#summary)
- [References](#references)
- [How to use](#how-to-use)

## Summary

Example repository showcasing the utilization of logging and monitoring solutions, interfacing with them through backend services.

## References

TBD

## How to use

### Prometheus

#### On Unix systems (Linux Ubuntu, Linux debian or MacOS versions)

Build and run the docker-compose network:

```sh
docker-compose up -d --build # On docker versions `docker compose up -d --build`
```

Checkout the Grafana dashboard `localhost:9090` on Unix systems. You can add new dashboards.

#### On Windows systems with Virtual Box enabled Docker

Mounting is an issues therefore checkout comments in the [docker-compose.yml](./docker-compose.yml). Therefore comment out lines in regards to volumes.

```sh
docker-compose up -d --build 
docker ps # Resolve container id of prometheus container
docker exec -it <prometheus container id> bash
# Manually update the scrape_config according to the [prometheus.yml](./prometheus/prometheus.yml) with `vi` cli tool
# Exit out of the container terminal. 
docker restart restart <prometheus container id>
```

After restarting Prometheus should be able to discover the metrics endpoints. 

#### Results

##### ASP .NET Core HelloWorld service metrics endpoints

![ASP .NET Core HelloWorld service metrics endpoints](./images/csharp-metrics-endpoint.PNG)

##### Prometheus metric for total requests received

![Prometheus metric for total requests received](./images/prometheus-metric-http_requests_received_total.PNG)

##### Grafana sample dashboard

![Grafana sample dashboard](./images/grafana-sample-dashboard.PNG)