![Dart Spatial Nigeria Limited](https://dartspatial.com.ng/log.png)

### 👋 Hi there!  
[Dart Spatial](http://dartspatial.com.ng/)
***
#### Application file structure


```yaml {.code-highlight}

darts_location_service
        api\
            service_api.py
        app\
            main.py
        connection/
            connect_config.py
            posgresql.py
            redis_connection.py
            test_connection.py
        data_model\
            http_response.py
            redis_model.py
            sqlalchemy_model.py
        di\
            app_di.py
        oauth\
            oauth2
        use_cases\
            continent_service.py
            country_service.py
            local_govt_service.py
            state_service.py
    .dockerignore
    .env
    .gitignore
    constants.py
    docker-compose.yml.j2
    dockerfile
    README.md
    requirements.txt
    secrets.yml
    table.sql


```
🚀
Run docker compose for redis 
> docker-compose -f redis-compose.yml up -d

Run docker compose for postgresql
> docker-compose -f postgresql_compose.yml up -d

Run docker compose for fastApi
> docker-compose -f fastapi-compose.yml up -d

start fast Api without docker for a testing purpose 
> uvicorn app.main:app --reload --port 8085

#### Application feature

- Redis port number 6310
- fastApi port number 8080


### feat: Completed Location microservice
This commit marks the completion of the location microservice. 

feature include:

- fastApi restFul Api
- Implemented CRUD operations for managing user location
- Added endpoints for retrieving continent, country, state and local goverment location
- Integrated JWT-based authentication and authorization middleware
- Implemented input validation and error handling
- Documented API endpoints using OpenAPI specifications
- Optimized database with sqlalchemy
- add redis to cache data
- postgreSQL

### using Ansible for securing the container sensitive data
>install Ansible
```
pip install ansible
```

encrypt a yaml file (secrets.yml) with ansible
```
ansible-vault encrypt secrets.yml
```

view the content of the encrypted file
```
ansible-vault view  secrets.yml
```

edit the  content of the encrypted file
```
ansible-vault edit  secrets.yml
```

decrypt the encrypted file
```
ansible-vault decrypt secrets.yml
```



Your docker-compose.yml.j2 file is a Jinja2 
template used to generate a Docker Compose 
configuration file dynamically. It appears to
be configured to inject environment variables 
into the Docker containers defined within the 
services section.
