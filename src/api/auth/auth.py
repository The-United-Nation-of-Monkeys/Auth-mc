from fastapi import APIRouter, Request, Depends, HTTPException, status, Response, Cookie
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.db.configuration import get_session
from src.db.models.admin import Table_Admins
from src.api.security.token import encode, decode
from src.api.security.password import check_password
from src.config import settings
from src.api.responses import *

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/login")
async def login(user_data: Annotated[HTTPBasicCredentials, Depends(HTTPBasic())], 
                response: Response, 
                session: AsyncSession = Depends(get_session)
                ):
    data = await session.execute(select(Table_Admins.password, Table_Admins.id, Table_Admins.role, Table_Admins.active)
                                 .where(Table_Admins.username == user_data.username))
    data = data.mappings().first()
    
    if not data:
        return status_error_401()
    
    if not check_password(user_data.password, data.password):
        return status_error_401()
    
    if not data.active:
        return status_error_403()
    
    payload = {
        "sup": data.id,
        "role": data.role.value
    }
    
    access_token = await encode(settings.auth.type_token.access, payload)
    refresh_token = await encode(settings.auth.type_token.refresh, payload)
    
    response.set_cookie(settings.auth.type_token.access, access_token)
    response.set_cookie(settings.auth.type_token.refresh, refresh_token)
    
    return {"status": "success"}  

@router.get("/access")
async def get_access(response: Response, 
                     request: Request,
                     session: AsyncSession = Depends(get_session) 
                     ):
    refresh_token = request.cookies.get(settings.auth.type_token.refresh)
        
    if not refresh_token:
        return status_error_401()
    
    try:
        payload = await decode(refresh_token)
        
    except:
        return status_error_401()
    

    user_data = await session.execute(select(Table_Admins.active)
                            .where(Table_Admins.id == payload["sup"]))
    user_data = user_data.mappings().first()
        
    if not user_data.active:
        return status_error_403()
    
    new_payload = {
        "sup": payload["sup"],
        "role": payload["role"],
    }
    
    new_access_token = await encode(settings.auth.type_token.access, new_payload)
    new_refresh_token = await encode(settings.auth.type_token.refresh, new_payload)

    
    response.set_cookie(settings.auth.type_token.access, new_access_token)
    response.set_cookie(settings.auth.type_token.refresh, new_refresh_token)
     
    return {"status": "success"}
     
    
@router.get("/logout")
async def logout(response: Response):
    response.set_cookie(settings.auth.type_token.access, None)
    response.set_cookie(settings.auth.type_token.refresh, None)
    
    return {"status": "success"}
    
