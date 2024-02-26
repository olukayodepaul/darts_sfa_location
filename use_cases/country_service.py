from sqlalchemy.orm import Session
from data_model import sqlalchemy_model as schemas 
from data_model.http_response import http_message, http_data, http_exception_404
from typing import Dict


class CountryService:
    
    def __init__(self, db: Session, payload: Dict):
        self.db = db
        
    def get_all_country(self):
        
        get_data = self.db.query(schemas.Country).all()
        if not get_data:
            raise http_exception_404(app_message='Country not found', app_status='Error')
        
        response_builder = {
            **http_message(app_message='Country found', app_status='Successful'),
            **http_data()
        }
        
        
        response_builder.update({"data": get_data})
        return {"detail":response_builder}
        
        
    def get_country(self, continent_id: int):
        
        get_data = self.db.query(schemas.Country).filter(schemas.Country.continent_id == continent_id).all()
        
        if not get_data:
            raise http_exception_404(app_message='Country not found', app_status='Error')
        
        response_builder = {
            **http_message(app_message='Country found', app_status='Successful'),
            **http_data()
        }
        
        response_builder.update({"data": get_data})
        return {"detail":response_builder}