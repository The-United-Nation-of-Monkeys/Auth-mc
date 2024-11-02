from fastapi import APIRouter, Request, Depends, HTTPException, status, Response, Cookie
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from sqlalchemy.exc import IntegrityError

from src.db.configuration import get_session
from src.db.models.users import Table_Users
from src.db.models.roles import *
from src.api.security.token import encode, decode
from src.api.security.password import check_password, encode_password
from src.config import settings
from src.api.responses import *
from src.api.auth.schemas import *
from src.broker.producer import Broker


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/login")
async def login(user_data: Annotated[HTTPBasicCredentials, Depends(HTTPBasic())], 
                response: Response, 
                session: AsyncSession = Depends(get_session)
                ):
    data = await session.execute(select(Table_Users.password, Table_Users.id, Table_Users.active, Table_Roles.role)
                                 .join(Table_Roles, Table_Roles.id == Table_Users.role_id)
                                 .where(Table_Users.login == user_data.username))
    
    data = data.mappings().first()
    
    if not data:
        return status_error_401()
    
    if not check_password(user_data.password, data.password):
        return status_error_401()
    
    if not data.active:
        return status_error_403()
    
    payload = {
        "sup": str(data.id),
        "role": data.role
    }
    
    access_token = await encode(settings.auth.type_token.access, payload)
    refresh_token = await encode(settings.auth.type_token.refresh, payload)
    
    response.headers.append("accessToken", "Bearer" + access_token)
    
    return status_success_200(refresh_token)

@router.post("/register")
async def get_access(user_data: Schema_Register,
                     session: AsyncSession = Depends(get_session) 
                     ):
    role = await session.execute(select(Table_Roles.id, Table_Roles.role, Table_Roles.special)
                                 .where(Table_Roles.role == user_data.role))
    try:
        role = role.mappings().first()
        role_id = role.id

    except AttributeError:
        return status_error_400("invalid role")
    password = encode_password(user_data.password)
    
    try:
        if role.special:
            user_id = await session.execute(insert(Table_Users).values({
                Table_Users.login: user_data.login,
                Table_Users.password: password,
                Table_Users.role_id: role_id,
                Table_Users.active: False
            }).returning(Table_Users.id))
            detail = "register but not activate"

        else:
            user_id = await session.execute(insert(Table_Users).values({
                    Table_Users.login: user_data.login,
                    Table_Users.password: password,
                    Table_Users.role_id: role_id
                }).returning(Table_Users.id))
            detail = None

        await session.commit()
        
    except IntegrityError:
        return await status_error_409("invalid login")

    Broker.send_message('auth', user_data.model_dump())

    return status_success_200(detail)


@router.get("/role/all")
async def get_role(session: AsyncSession = Depends(get_session)):
    data = await session.execute(select(Table_Roles.role, Table_Roles.special))
    data = data.mappings().all()
    
    return status_success_200(data)
    
     



#кафка и подтверждение почты 