print("------------------ \n\n Start add data \n\n--------------")

from sqlalchemy import insert

import asyncio, sys, os

sys.path.append(os.path.join(sys.path[0][:-6]))

from src.db.configuration import async_session_factory
from src.security.password import encode_password
from src.db.models.roles import *

async def start():
    async with async_session_factory() as session:

        await session.execute(insert(Table_Roles).values({
            Table_Roles.role: Base_Roles.admin.value,
            Table_Roles.special: True
        }))
        await session.execute(insert(Table_Roles).values({
            Table_Roles.role: Base_Roles.teacher.value,
            Table_Roles.special: True
        }))
        await session.execute(insert(Table_Roles).values({
            Table_Roles.role: Base_Roles.student.value,
            Table_Roles.special: False
        }))
        
        
        await session.commit()
        
asyncio.run(start())

print("-------------------------------\n\nFinish add data \n\n ---------------------------------")