import os
from dotenv import load_dotenv
load_dotenv()

config = dict({
    "ps_sql": {
        "ps_user" : os.getenv("POSTGRES_USER"),
        "ps_password" : os.getenv("POSTGRES_PASSWORD"),
        "ps_host_name" : os.getenv("POSTGRES_HOST_NAME"),
        "ps_port" : os.getenv("POSTGRES_PORT"),
        "ps_db" : os.getenv("POSTGRES_DB")
    },
    "jwt":{
        "secret_key" :os.getenv("JWT_SECRET_KEY"),
        "algorithm": os.getenv("JWT_ALGORITHM")
        },
    "redis":{
        "host" :os.getenv("REDIS_HOST"),
        "port": os.getenv("REDIS_PORT")
    }})