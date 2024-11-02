from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy import update

from src.api.responses import *
from src.api.confirmation.mail import *
from src.db.configuration import get_session
from src.db.models import Table_Users, Table_Roles
from sqlalchemy.exc import DBAPIError

router = APIRouter(
    prefix="/confirmation",
    tags=["Confirmation"]
)

@router.get("/access")
async def access_user(id: str, session: AsyncSession = Depends(get_session)):
    query = select(Table_Roles.special).join(Table_Users, Table_Users.role_id == Table_Roles.id).where(Table_Users.id == id)
    try:
        user_role = await session.execute(query)

    except DBAPIError:
        return status_error_400()

    if user_role.scalar():
        return status_error_403()

    update_query = update(Table_Users).values(active = True).where(Table_Users.id == id)
    await session.execute(update_query)
    await session.commit()

    return status_success_200()