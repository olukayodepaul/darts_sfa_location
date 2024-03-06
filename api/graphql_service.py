# from fastapi import APIRouter, Request
# from fastapi.responses import JSONResponse
# from starlette.graphql import GraphQLApp
# from use_cases.location_search_service import schema

# router = APIRouter()

# @router.post("/graphql")
# async def graphql(request: Request):
#     return GraphQLApp(schema=schema)(request)





from fastapi import APIRouter
from starlette.graphql import GraphQLApp
from use_cases.location_search_service import schema

router = APIRouter()

@router.post("/graphql")
async def graphql():
    return GraphQLApp(schema=schema)
