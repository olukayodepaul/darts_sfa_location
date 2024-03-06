"""
API service module for handling continent, country, state, and local government services.
"""

from fastapi import APIRouter, Depends, status
from use_cases.continent_service import ContinentService
from use_cases.country_service import CountryService
from use_cases.state_service import StateService
from use_cases.local_govt_service import LocalGovtService
from di.app_di import continent_service, country_service, state_service, local_govt_service

router = APIRouter()


@router.get("/continent", status_code=status.HTTP_200_OK)
async def all_continent(injection: ContinentService = Depends(continent_service)):
    """Get all continents."""
    return injection.all_continent()


@router.get("/continent/{continent_id}", status_code=status.HTTP_200_OK)
async def get_all_continent(
    continent_id: int,
    injection: ContinentService = Depends(continent_service)
):
    """Get continent by ID."""
    return injection.get_continent(continent_id)


@router.get("/country", status_code=status.HTTP_200_OK)
async def all_country(injection: CountryService = Depends(country_service)):
    """Get all countries."""
    return injection.get_all_country()


@router.get("/country/{continent_id}", status_code=status.HTTP_200_OK)
async def get_all_country(
    continent_id: int,
    injection: CountryService = Depends(country_service)
):
    """Get countries by continent ID."""
    return injection.get_country(continent_id)


@router.get("/state", status_code=status.HTTP_200_OK)
async def is_all_state(injection: StateService = Depends(state_service)):
    """Get all states."""
    return injection.all_state()


@router.get("/state/{country_id}", status_code=status.HTTP_200_OK)
async def is_first_state(
    country_id: int,
    injection: StateService = Depends(state_service)
):
    """Get first state by country ID."""
    return injection.first_state(country_id)


@router.get("/localgovt/{state_id}", status_code=status.HTTP_200_OK)
async def all_local_govt(
    state_id: int,
    injection: LocalGovtService = Depends(local_govt_service)
):
    """Get all local governments by state ID."""
    return injection.get_local_govt(state_id)
