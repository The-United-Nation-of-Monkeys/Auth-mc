from fastapi import Depends, APIRouter
from fastapi.responses import HTMLResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy.exc import DBAPIError

from src.api.responses import *
from src.db.configuration import get_session
from src.db.models import Table_Users, Table_Roles
from src.api.confirmation.forms import active_account_form


router = APIRouter(
    prefix="/confirmation",
    tags=["Confirmation"]
)

@router.get("/access")
async def access_user(id: str, session: AsyncSession = Depends(get_session)):
    query = select(Table_Roles.special).join(Table_Users,
                                             Table_Users.role_id == Table_Roles.id).where(Table_Users.id == id)
    try:
        user_role = await session.execute(query)

    except DBAPIError:
        return status_error_400()

    if user_role.scalar():
        return status_error_403()

    update_query = update(Table_Users).values(active = True).where(Table_Users.id == id)
    await session.execute(update_query)
    await session.commit()

    return HTMLResponse(active_account_form)

@router.get("/new/password")
async def new_password(token: str, email: str):
    pass