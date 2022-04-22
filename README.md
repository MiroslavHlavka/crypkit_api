# Crypkit API
Simple API for managing cryptocurrencies

# What to do better
## Grafana / Metrics
I thought that I would download some premade dashboard for fastapi/starlette but there wasnt any 
that would work out of the box with prometheus exporter lib that I chose -.- so the graphs are 
very simple and not polished.

Default metric labels from starlette exporter are not great, so I would tweak that

## Tests
To have some meaningful tests I would need to create db handling, fill some test data into a 
database etc

# Creating DB structure with alembic
```bash
docker-compose up alembic 
```

## How to run locally
```bash
docker-compose up api 
```

# Documentation
You can find documentation on endpoint /-/docs for example:
```
http://0.0.0.0:8080/-/docs
```

# Formatting
Every code is formatted with Isort and Black

# Grafana
```
http://0.0.0.0:3000
```
Username and password is default (admin, admin #security :)

# Metrics via Prometheus
```
http://0.0.0.0:9090
```