from fastapi import APIRouter, Depends, Request
from fastapi_cache.decorator import cache
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, update, update, delete

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
@router.get("/cat/all/breeds")
async def get_all_breeds(request: Request,
                         session: AsyncSession = Depends(get_session)):
    token = request.cookies.get(settings.auth.type_token.access)
    
    await check_permission(Roles.admin.value, token) 
    
    data = await session.execute(select(Table_Cats.breed))
    
    return status_success_200({"breeds": data.scalars().unique().all()})

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
@router.get("/cat/all/filter/breed")
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

@router.post("/cat/add")
async def add_cat(
    request_data: Default_Cat_Schema,
    request: Request,
    session: AsyncSession = Depends(get_session)
):
    token = request.cookies.get(settings.auth.type_token.access)

    await check_permission(Roles.admin.value, token) 
    
    await session.execute(insert(Table_Cats).values({
        Table_Cats.age: request_data.age,
        Table_Cats.breed: request_data.breed,
        Table_Cats.color: request_data.color,
        Table_Cats.description: request_data.description
    }))
    await session.commit()
    
    return status_success_200()

@router.put("/cat/update")
async def update_cat(
    id: int,
    request_data: Default_Cat_Schema,
    request: Request,
    session: AsyncSession = Depends(get_session)
):
    token = request.cookies.get(settings.auth.type_token.access)

    await check_permission(Roles.admin.value, token) 
    
    await session.execute(update(Table_Cats).values({
        Table_Cats.age: request_data.age,
        Table_Cats.breed: request_data.breed,
        Table_Cats.color: request_data.color,
        Table_Cats.description: request_data.description
    }).where(Table_Cats.id == id))
    
    await session.commit()
    
    return status_success_200()

@router.delete("/cat/del/{id}")
async def del_cat(
    id: int,
    request: Request,
    session: AsyncSession = Depends(get_session)
):
    token = request.cookies.get(settings.auth.type_token.access)

    await check_permission(Roles.admin.value, token) 
    
    await session.execute(delete(Table_Cats).where(Table_Cats.id == id))
    await session.commit()
    
    return status_success_200()