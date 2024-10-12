from fastapi import APIRouter, Request, Depends, HTTPException, status, Response, Cookie
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert

from db.configuration import get_session
from db.models.users import Table_Users
from db.models.roles import *
from api.security.token import encode, decode
from api.security.password import check_password, encode_password
from config import settings
from api.responses import *
from api.auth.schemas import Schema_Register

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/login")
async def login(user_data: Annotated[HTTPBasicCredentials, Depends(HTTPBasic())], 
                response: Response, 
                session: AsyncSession = Depends(get_session)
                ):
    data = await session.execute(select(Table_Users.password, Table_Users.id, Table_Users.role_id, Table_Users.active)
                                 .where(Table_Users.login == user_data.username))
    data = data.mappings().first()
    
    if not data:
        return status_error_401()
    
    if not check_password(user_data.password, data.password):
        return status_error_401()
    
    if not data.active:
        return status_error_403()
    
    payload = {
        "sup": data.id,
        "role": data.role_id
    }
    
    access_token = await encode(settings.auth.type_token.access, payload)
    refresh_token = await encode(settings.auth.type_token.refresh, payload)
    
    response.set_cookie(settings.auth.type_token.access, access_token)
    response.set_cookie(settings.auth.type_token.refresh, refresh_token)
    
    return {"status": "success"}  

@router.post("/register")
async def get_access(user_data: Schema_Register,
                     session: AsyncSession = Depends(get_session) 
                     ):
    role = await session.execute(select(Table_Roles.id, Table_Roles.role).where(Table_Roles.role == user_data.role))
    
    try:
        role = role.mappings().first()
        role_id = role.id
        
        role = role.role
        
    except:
        return status_error_400("invalid role")
    
    if role == Base_Roles.admin.value : return status_error_400("invalid  role")
    
    
    password = encode_password(user_data.password)
    
    try: 
        await session.execute(insert(Table_Users).values({
            Table_Users.login: user_data.login,
            Table_Users.password: password,
            Table_Users.role_id: role_id
        }))
    
        await session.commit()
        
    except:
        return await status_error_400("invalid login")
    
    return status_success_200()
    
     



#вернуть все роли, кафка, токен пихать в barer 