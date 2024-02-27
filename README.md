![Dart Spatial Nigeria Limited](https://dartspatial.com.ng/log.png)

### 👋 Hi there!  
[Dart Spatial](http://dartspatial.com.ng/)
***
#### Application file structure


```yaml {.code-highlight}
dart_spatial_sfa_company_service
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
            model.py
    kafka\
    venv\
    .dockerignore
    .env
    .gitignore
    configuration.py
    docker-compose.yml
    dockerfile
    kafka_producer.py
    README.nd
    requirements.txt
    SQL.sql
    util.py
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


### feat: Completed company microservice
This commit marks the completion of the company microservice. 

feature include:

- Implemented CRUD operations for managing companies
- Added endpoints for adding, retrieving, updating, and deleting companies
- Integrated JWT-based authentication and authorization middleware
- Implemented input validation and error handling
- Documented API endpoints using OpenAPI specifications
- Optimized database queries
- Refactored code for readability and maintainability
- add redis to cache data
- README file for details

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

