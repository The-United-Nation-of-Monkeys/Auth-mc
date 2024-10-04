from sqlalchemy import select

from src.api.security.token import decode
from src.api.responses import *
from src.db.configuration import async_session_factory
from src.db.models.admin import Table_Admins


async def check_permission(permission: str, token: str | bytes | None = None):
    if not token:
        return status_error_401()
    
    try:
        data = await decode(token)
        
    except:
        return status_error_401()
    
    async with async_session_factory() as session:
        user_data = await session.execute(select(Table_Admins.role)
                               .where(Table_Admins.id == data["sup"]))
        user_data = user_data.mappings().first()
    
        if data["role"] != permission != user_data.role.value:
            return status_error_403()
    
    return True