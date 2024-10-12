from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from sqlalchemy import select
import uvicorn

from db.models.roles import Table_Roles
from db.configuration import async_session_factory
from api.auth.auth import router as auth_router

from config import settings

app = FastAPI(
    title="cats", openapi_prefix="/api/v1"
    )

@app.get("/")
def title():
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content="Auth mc")

@app.get("/test")
async def test():
    async with async_session_factory() as session:
        role = await session.execute(select(Table_Roles.id, Table_Roles.role))
        role2 = await session.execute(select(Table_Roles.id, Table_Roles.role).where(Table_Roles.role == "student"))
        role3 = await session.execute(select(Table_Roles.id, Table_Roles.role).where(Table_Roles.role == "student"))
        role4 = await session.execute(select(Table_Roles.id, Table_Roles.role).where(Table_Roles.role == "student"))
        role5 = await session.execute(select(Table_Roles.id, Table_Roles.role).where(Table_Roles.role == "student"))
        role6 = await session.execute(select(Table_Roles.id, Table_Roles.role).where(Table_Roles.role == "student"))
        role7 = await session.execute(select(Table_Roles.id, Table_Roles.role).where(Table_Roles.role == "student"))
        role8 = await session.execute(select(Table_Roles.id, Table_Roles.role).where(Table_Roles.role == "student"))
        
        a = role2.mappings().all()
        print(a[0].id)
        print(role)
        print(role.scalars().all())
        print(role2.mappings().all())
        print(role3.mappings().first())
        print(role4.mappings().fetchall())
        print(role5.all())
        print(role6.first())
        print(role7.scalar())
        print(role8.mappings().fetchmany())
        
app.include_router(auth_router)


def run():
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")

if __name__ == "__main__":
    run()