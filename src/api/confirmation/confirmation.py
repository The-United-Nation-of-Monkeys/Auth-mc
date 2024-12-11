from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from sqlalchemy import update
from sqlalchemy.exc import DBAPIError

from src.api.responses import *
from src.db.configuration import get_session
from src.db.models import Users, Roles
from src.api.confirmation.responses import HtmlResponseStatus


router = APIRouter(
    prefix="/confirmation",
    tags=["Confirmation"]
)


@router.get("/access")
async def access_user(id: str, session: AsyncSession = Depends(get_session)):
    query = select(Roles.special).join(Users, Users.role_id == Roles.id).where(Users.id == id)
    try:
        user_role = await session.execute(query)

    except DBAPIError:
        return status_error_400()

    if user_role.scalar():
        return status_error_403()

    update_query = update(Users).values(active = True).where(Users.id == id)
    await session.execute(update_query)
    await session.commit()

    return HtmlResponseStatus.account_info("активирована")


@router.get("/delete")
async def delete_account(id: str, session: AsyncSession = Depends(get_session)):
    check_query = select(Users.active).where(Users.id == id)
    active_query = await session.execute(check_query)
    active = active_query.scalar()
    
    if active:
        return HtmlResponseStatus.error_active()
    
    query = delete(Users).where(Users.id == id, Users.active == False)
    await session.execute(query)
    await session.commit()
    return HtmlResponseStatus.account_info("удалена")
