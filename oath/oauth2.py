from jose import jwt,  JWTError
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from data_model.http_response import http_exception_401
from datetime import  datetime
from connection.connect_config import config

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = config["jwt"]['secret_key']
ALGORITHM = config["jwt"]['algorithm']

def create_access_token(payload: dict):
    to_encode = payload.copy()
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str, credential_exception):
    
    try:
        
        pay_load = jwt.decode(token, SECRET_KEY, ALGORITHM)
        exp = pay_load.get("exp")
        
        if exp is None or datetime.utcfromtimestamp(exp) < datetime.utcnow():
            raise credential_exception
        
        token_date = pay_load
        
    except JWTError:
        raise credential_exception
    
    return token_date

def get_current_user(token: str = Depends(oauth2_scheme)):
    credential_exception = http_exception_401()
    return verify_access_token(token, credential_exception)