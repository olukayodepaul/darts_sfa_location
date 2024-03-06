from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import api_service, graphql_service
from connection import posgresql as models

connection = models.Base.metadata.create_all(bind=models.engine)

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
app.include_router(graphql_service.router, prefix="/location", tags=["location"]) 