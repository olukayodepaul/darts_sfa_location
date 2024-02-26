from sqlalchemy.orm import Session
from data_model import sqlalchemy_model as schemas 
from data_model.http_response import http_message, http_data, http_exception_404
import json
from data_model.redis_model import serialize_localgovt
from connection.redis_connection import search, add
from typing import Dict


class LocalGovtService:
    
    def __init__(self, db: Session, payload: Dict):
        self.db = db
        
    def get_local_govt(self, state_id: int):
        
        redis_key = f"localgovt?state_id={state_id}"
        
        search_redis = search(redis_key)
        
        if search_redis is not None:
            get_data = search_redis
        else:
            
            get_data = self.db.query(schemas.LocalGovt).filter(schemas.LocalGovt.states_id == state_id).all()
            
            if not get_data:
                raise http_exception_404(app_message='Local Government not found', app_status='Error')
            
            serialized_locat_govt_data = [serialize_localgovt(localgovt) for localgovt in get_data]
            local_govt_data_json = json.dumps(serialized_locat_govt_data)
            add(redis_key, local_govt_data_json)
            
            
        response_builder = {
            **http_message(app_message='Country found', app_status='Successful'),
            **http_data()
        }
        
        response_builder.update({"data": get_data})
        return response_builder