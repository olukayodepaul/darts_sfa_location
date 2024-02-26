from fastapi import APIRouter, Depends, status
from use_cases.continent_service import ContinentService
from use_cases.country_service import CountryService
from di.app_di import continent_service, country_service

router = APIRouter()


@router.get("/continent", status_code=status.HTTP_200_OK)
async def all_continent(injection: ContinentService = Depends(continent_service)):
    return injection.all_continent()

@router.get("/continent/{id}", status_code=status.HTTP_200_OK)
async def get_all_continent(id: int, injection: ContinentService = Depends(continent_service)):
    return injection.get_continent(id)

@router.get("/country", status_code=status.HTTP_200_OK)
async def all_country(injection: CountryService = Depends(country_service)):
    return injection.get_all_country()

@router.get("/country/{continent_id}", status_code=status.HTTP_200_OK)
async def get_all_country(continent_id: int, injection: CountryService = Depends(country_service)):
    return injection.get_country(continent_id)

# @router.get("/state", status_code=status.HTTP_200_OK)
# async def is_all_state(injection: State_Service = Depends(state_service)):
#     return injection.all_state()

# @router.get("/state/{country_id}", status_code=status.HTTP_200_OK)
# async def is_first_state(country_id: int, injection: State_Service = Depends(state_service)):
#     return injection.first_state(country_id)

# @router.get("/localgovt/{state_id}", status_code=status.HTTP_200_OK)
# async def all_local_govt(state_id: int, injection: Local_Govt_Service = Depends(local_govt_service)):
#     return injection.get_local_govt(state_id)

