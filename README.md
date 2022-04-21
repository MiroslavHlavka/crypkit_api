# Crypkit API
Simple API for managing cryptocurrencies

# Creating DB structure with alembic
```bash
docker-compose run alembic update head 
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