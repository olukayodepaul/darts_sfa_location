from sqlalchemy.orm import Session
from data_model import sqlalchemy_model as schemas 
from data_model.http_response import http_message, http_data, http_exception_404
from typing import Dict


class ContinentService:
    
    def __init__(self, db: Session, payload: Dict):
        self.db = db
        
    def all_continent(self):
        
        get_data = self.db.query(schemas.Continent).all()
        if not get_data:
            raise http_exception_404(app_message='Continent not found', app_status='Error')
        
        response_builder = {
            **http_message(app_message='Continent found', app_status='Successful'),
            **http_data()
        }
        
        response_builder.update({"data": get_data})
        return {"detail":response_builder}
        
        
    def get_continent(self, id: int):
        
        get_data = self.db.query(schemas.Continent).filter(schemas.Continent.id == id).first()
        
        if not get_data:
            raise http_exception_404(app_message='Continent not found', app_status='Error')
        
        response_builder = {
            **http_message(app_message='Continent found', app_status='Successful'),
            **http_data()
        }
        
        response_builder.update({"data": get_data})
        return {"detail":response_builder}