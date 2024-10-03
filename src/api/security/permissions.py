from src.api.security.token import decode
from src.api.responses import *


async def check_permission( permission: str, token: str | bytes | None = None,):
    if not token:
        return status_error_401()
    
    try:
        data = await decode(token)
        
    except:
        return status_error_401()
    
    if data["role"] != permission:
        return status_error_403()
    
    return True