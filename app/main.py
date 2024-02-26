from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import api_service 
from connection import posgresql as models
from connection.test_connection import test_connection
from connection import connect_config

connection = models.Base.metadata.create_all(bind=models.engine)
test_connection()


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_service.router, prefix="/location", tags=["location"])