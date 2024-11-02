from sqlalchemy import select
from functools import wraps
from fastapi import Request

from src.api.security.token import decode
from src.api.responses import *
from src.db.configuration import async_session_factory
from src.config import settings

def check_person(func):
    
    @wraps
    async def wrapper(*args, **kwargs):
        token: Request = kwargs.get("request")
        token = token.cookies.get(settings.auth.type_token.access)
        
        if not token:
            status_error_401()    