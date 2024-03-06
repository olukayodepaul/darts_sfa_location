"""
Module representing all http response.
"""

from typing import Dict
from fastapi import HTTPException, status

def http_exception_404(app_message: str, app_status: str) -> HTTPException:
    """
    Create a 404 HTTPException with the specified app_message and app_status.
    """
    http_exception = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=http_message(app_message=app_message, app_status=app_status)
    )
    return http_exception


def http_message(app_message: str, app_status: str) -> Dict:
    """
    Create a dictionary containing the specified app_message and app_status.
    """
    return {
        "message": app_message,
        "status": app_status,
    }


def http_data() -> Dict:
    """
    Create an empty dictionary for HTTP response data.
    """
    return {
        "data": []
    }


def http_exception_401() -> HTTPException:
    """
    Create a 401 HTTPException for unauthorized access.
    """
    http_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=http_message(app_message="Validation Token", app_status="Error"),
        headers={"WWW-Authenticate": "Bearer"}
    )
    return http_exception
