from sqlalchemy import select
from functools import wraps
from fastapi import Request

from src.security.token import decode
from src.api.responses import *
from src.db.configuration import async_session_factory
from src.config import settings
from src.api.responses import status_error_401, status_error_403

def permissions(role: str):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            token: str = kwargs.get("token")
            if not token:
                status_error_401()
            
            try:
                payload = await decode(token.credentials)
            except Exception as e:
                status_error_401()
                
            if payload.get("role") != role:
                status_error_403()
            
            return await func(*args, **kwargs)    
        return wrapper
    return decorator