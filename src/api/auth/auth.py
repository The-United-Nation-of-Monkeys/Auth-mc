from fastapi import APIRouter, Request, Depends, HTTPException, status, Response
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from sqlalchemy.exc import IntegrityError
from pydantic import EmailStr

from src.db.configuration import get_session
from src.db.models.users import Users
from src.db.models.roles import *
from src.security.token import encode, decode
from src.security.password import check_password, encode_password
from src.config import settings, security
from src.api.responses import *
from src.api.auth.schemas import *
from src.broker.producer import Broker
from src.notification.mail import mail


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/login")
async def login(user_data: UserLogin, 
                session: AsyncSession = Depends(get_session)
                ):
    data = await session.execute(select(Users.password, Users.id, Users.active, Users.banned, Roles.role)
                                 .join(Roles, Roles.id == Users.role_id)
                                 .where(Users.login == user_data.login.lower()))
    
    data = data.mappings().first()
    
    if not data or not check_password(user_data.password, data.password):
        return status_error_401()

    elif not data.active or data.banned:
        return status_error_403("not active account")
    
    payload = {
        "sup": str(data.id),
        "role": data.role
    }
    
    access_token = await encode(settings.auth.type_token.access, payload)
    refresh_token = await encode(settings.auth.type_token.refresh, payload)
        
    return status_success_200({"refresh": refresh_token, "access": access_token})

@router.post("/register")
async def get_access(user_data: SchemaRegister,
                     session: AsyncSession = Depends(get_session) 
                     ):
    role = await session.execute(select(Roles.id, Roles.role, Roles.special)
                                 .where(Roles.role == user_data.role))
    try:
        role = role.mappings().first()
        role_id = role.id

    except AttributeError:
        return status_error_400("invalid role")

    password = encode_password(user_data.password)
    
    try:
        user_id = await session.execute(insert(Users).values({
            Users.login: user_data.login.lower().strip(),
            Users.password: password,
            Users.role_id: role_id,
            Users.name: user_data.name
        }).returning(Users.id))

        detail = {"message": "register but not activate"}
        user_id = user_id.scalar()
        
    except IntegrityError:
        return await status_error_409("invalid login")

    mail.send_register_mail(user_data.login, name=user_data.name, id=user_id, special=role.special)
        
    detail.update(special=role.special)
    transfer_user_data = user_data.model_dump(exclude={"password"})
    transfer_user_data.update(
        specialized=role.special,
        user_id=str(user_id)
    )

    await session.commit()
    Broker.send_message('auth', transfer_user_data)
    return status_success_201(detail)


@router.get("/register/repeat", status_code=status.HTTP_204_NO_CONTENT)
async def repeat_register(email: str, session: AsyncSession = Depends(get_session)) -> None:
    query = (select(Users.id, Users.active, Users.banned, Users.name, Roles.special)
    .join(Roles, Roles.id == Users.role_id).where(Users.login == email.lower()))
    user_info = await session.execute(query)
    user_info = user_info.mappings().first()
    
    try:
        if user_info["active"]:
            return status_error_400("account is active")
        elif user_info["banned"]:
            return status_error_400("account is blocked")
    except TypeError:
        return status_error_400("account undefined")
        
    mail.send_register_mail(recipient=email, name=user_info.name, id=user_info.id, special=user_info.special)
        
    


@router.get("/role/all")
async def get_role(session: AsyncSession = Depends(get_session)):
    data = await session.execute(select(Roles.role, Roles.special, Roles.name))
    data = data.mappings().all()
    
    return status_success_200(data)


@router.get("/refresh")
async def get_access_token(refresh_token: Annotated[HTTPBasicCredentials, Depends(security)],
                           response: Response,
                           session: AsyncSession = Depends(get_session)):
    try:
        payload = await decode(refresh_token.credentials)
    
    except Exception:
        status_error_401()
        
    query = (select(Users.password, Users.id, Users.banned,Roles.role)
    .join(Roles, Roles.id == Users.role_id)
    .where(Users.id == payload["sup"]))
    user = await session.execute(query)
    user_info = user.mappings().first()
    
    if not user_info:
        status_error_403("invalid account")
    
    if user_info["banned"]:
        status_error_403("blocked")
        
    new_payload = {
        "sup": str(user_info["id"]),
        "role": user_info["role"]
    }
    
    new_refresh_token = await encode(settings.auth.type_token.refresh, new_payload)
    new_access_token = await encode(settings.auth.type_token.access, new_payload)
    
    return status_success_200({"refresh": new_refresh_token, "access": new_access_token})
    



