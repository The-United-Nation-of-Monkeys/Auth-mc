from sqlalchemy import select
from functools import wraps
from fastapi import Request

from api.security.token import decode
from api.responses import *
from db.configuration import async_session_factory
from config import settings

def check_person(func):
    
    @wraps
    async def wrapper(*args, **kwargs):
        token: Request = kwargs.get("request")
        token = token.cookies.get(settings.auth.type_token.access)
        
        if not token:
            status_error_401()    