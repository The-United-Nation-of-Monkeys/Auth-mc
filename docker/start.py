print("------------------ \n\n Start add data \n\n--------------")

from sqlalchemy import insert

import asyncio, sys, os

sys.path.append(os.path.join(sys.path[0][:-6]))

from src.db.configuration import async_session_factory
from src.security.password import encode_password
from src.db.models.roles import *

async def start():
    async with async_session_factory() as session:

        await session.execute(insert(Roles).values({
            Roles.role: BaseRoles.admin.value,
            Roles.special: True,
            Roles.name: "Админ"
        }))
        await session.execute(insert(Roles).values({
            Roles.role: BaseRoles.teacher.value,
            Roles.special: True,
            Roles.name: "Учитель"
        }))
        await session.execute(insert(Roles).values({
            Roles.role: BaseRoles.student.value,
            Roles.special: False,
            Roles.name: "Студент"
        }))
        
        
        await session.commit()
        
asyncio.run(start())

print("-------------------------------\n\nFinish add data \n\n ---------------------------------")