
from sqlalchemy.orm import Session
from data_model import sqlalchemy_model as schemas 
from data_model.http_response import http_message, http_data, http_exception_404
from typing import Dict

class StateService:
    
    def __init__(self, db: Session, payload: Dict):
        self.db = db
        
    def all_state(self):
        
        get_data = self.db.query(schemas.State).all()
        if not get_data:
            raise http_exception_404(app_message='State not found', app_status='Error')
        
        response_builder = {
            **http_message(app_message='Country found', app_status='Successful'),
            **http_data()
        }
        
        response_builder.update({"data": get_data})
        return {"detail":response_builder}
        
        
    def first_state(self, country_id: int):
        
        get_data = self.db.query(schemas.State).filter(schemas.State.country_id == country_id).all()
        
        if not get_data:
            raise http_exception_404(app_message='State not found', app_status='Error')
        
        response_builder = {
            **http_message(app_message='Country found', app_status='Successful'),
            **http_data()
        }
        
        response_builder.update({"data": get_data})
        return {"detail":response_builder}