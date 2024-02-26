from fastapi import  HTTPException, status
import bcrypt
from typing import Dict


def http_exception_404(app_message: str , app_status:str) -> HTTPException:
    http_exception = HTTPException(
        status_code= status.HTTP_404_NOT_FOUND, 
        detail= {
            **http_message(app_message=app_message, app_status=app_status)
            }
        )
    return http_exception

def http_message(app_message:str, app_status:str) -> Dict:
    return {
        "message": app_message,
        "status": app_status,
    }
    
def http_data() -> Dict:
    return {
        "data" : []
    }
    
def http_exception_401() -> HTTPException:

    http_exception = HTTPException(
        status_code= status.HTTP_401_UNAUTHORIZED,
        detail= {
            **http_message(app_message="Validation Token", app_status="Error")
            },
        headers={
            "WWW-Authenticate": "Bearer"
        })
    return http_exception