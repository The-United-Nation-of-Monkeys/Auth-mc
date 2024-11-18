from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import EmailStr

from src.security.keys import generate_rand_key, encode_key, check_key
from src.notification.mail import send_switch_password_mail
from src.config import settings
from src.broker.redis import redis
from src.api.responses import status_error_400
from src.api.account.schemas import SSwitchPassword
from src.db.configuration import get_session


router = APIRouter(
    prefix="/account",
    tags=["Account"]
)

@router.get("/new/password", status_code=status.HTTP_200_OK)
async def new_password(email: EmailStr) -> None:
    secret_key = generate_rand_key()
    encode_secret_key = encode_key(secret_key)
    redis.set_value(key=email, value=encode_secret_key, expiration=600) 
    send_switch_password_mail(email, secret_key)
    
    
@router.patch("/new/password", status_code=status.HTTP_200_OK)
async def update_password(email: EmailStr, code: str, 
                          new_password: SSwitchPassword, 
                          session: AsyncSession = Depends(get_session)) -> None:
    hashed_code = redis.get_value(email)
    
    if not check_key(code, hashed_code):
        return status_error_400()
    
    pass
    