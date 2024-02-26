from fastapi import Depends
from sqlalchemy.orm import Session
from connection.posgresql import get_db
from oath.oauth2 import get_current_user
from use_cases.continent_service import ContinentService
from use_cases.country_service import CountryService
from use_cases.state_service import StateService
from use_cases.local_govt_service import LocalGovtService

def continent_service(db: Session = Depends(get_db), payload = Depends(get_current_user)):
    return ContinentService(db=db, payload = payload)

def country_service(db: Session = Depends(get_db), payload = Depends(get_current_user)):
    return CountryService(db=db, payload = payload)

def state_service(db: Session = Depends(get_db), payload = Depends(get_current_user)):
    return StateService(db=db, payload=payload)

def local_govt_service(db: Session = Depends(get_db), payload = Depends(get_current_user)):
    return LocalGovtService(db=db, payload=payload)
