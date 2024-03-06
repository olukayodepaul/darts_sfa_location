"""
GraphQL service module for handling GraphQL requests.
"""

from fastapi import APIRouter
from starlette.graphql import GraphQLApp
from use_cases.location_search_service import schema

router = APIRouter()

@router.post("/graphql")
async def graphql():
    """
    Handle GraphQL requests.
    
    Returns:
        GraphQLApp: GraphQL application.
    """
    return GraphQLApp(schema=schema)
