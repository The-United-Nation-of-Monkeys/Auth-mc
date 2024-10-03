from fastapi import APIRouter, Depends, Request
from fastapi_cache.decorator import cache
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, update

from src.db.configuration import get_session
from src.config import settings
from src.api.security.token import decode
from src.db.models.cats import *
from src.api.responses import *
from src.api.security.permissions import *
from src.db.roles import Roles
from src.api.cats.schemas import *

router = APIRouter(
    prefix="/cats",
    tags=["Cats"]
)


@cache(expire=10)
@router.get("/all/breeds")
async def get_all_breeds(request: Request,
                         session: AsyncSession = Depends(get_session)):
    token = request.cookies.get(settings.auth.type_token.access)
    
    await check_permission(Roles.admin.value, token) 
    
    data = await session.execute(select(Table_Cats.breed))
    
    return status_success_200({"breeds": data.unique().all()})

@cache(expire=10)
@router.get("/all/cats")
async def get_all_cats(
    request: Request,
    session: AsyncSession = Depends(get_session)
):
    token = request.cookies.get(settings.auth.type_token.access)

    await check_permission(Roles.admin.value, token) 

    data = await session.execute(select(
        Table_Cats.id,
        Table_Cats.age,
        Table_Cats.color,
        Table_Cats.description,
        Table_Cats.breed
    ))
    
    return status_success_200(data.mappings().all())

@cache(expire=10)
@router.get("/all/filter/breed/{breed}")
async def get_all_fil_breed(
    request: Request,
    breed: str | None = None,
    session: AsyncSession = Depends(get_session)
):
    token = request.cookies.get(settings.auth.type_token.access)

    await check_permission(Roles.admin.value, token) 
    
    data = await session.execute(select(
        Table_Cats.id,
        Table_Cats.age,
        Table_Cats.color,
        Table_Cats.description,
    ).where(Table_Cats.breed == breed))
    
    return status_success_200(data.mappings().all())
    
@cache(expire=10)
@router.get("/cat/{id}")
async def get_cat(
    id: int,
    request: Request,
    session: AsyncSession = Depends(get_session)
):
    token = request.cookies.get(settings.auth.type_token.access)

    await check_permission(Roles.admin.value, token) 
    
    data = await session.execute(select(Table_Cats).where(Table_Cats.id == id))
    
    return status_success_200(data.mappings().all())

@router.post("/add/cat")
async def add_cat(
    request_data: Add_Cat_Schema,
    request: Request,
    session: AsyncSession = Depends(get_session)
):
    pass