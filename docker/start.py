from sqlalchemy import insert

import asyncio, sys, os

sys.path.append(os.path.join(sys.path[0][:-6], "src"))

from db.configuration import async_session_factory
from db.models.admin import Table_Admins
from db.models.cats import Table_Cats
from api.security.password import encode_password

async def start():
    async with async_session_factory() as session:
        await session.execute(insert(Table_Admins).values({
            Table_Admins.username: "test",
            Table_Admins.password: encode_password("test")
        }))
        
        await session.execute(insert(Table_Cats).values({
            Table_Cats.age: 12,
            Table_Cats.color: "black",
            Table_Cats.description: "good cat",
            Table_Cats.breed: "Siamese"
        }))
        
        await session.execute(insert(Table_Cats).values({
            Table_Cats.age: 10,
            Table_Cats.color: "brown",
            Table_Cats.description: "good cat",
            Table_Cats.breed: "Siamese"
        }))

        await session.execute(insert(Table_Cats).values({
            Table_Cats.age: 2,
            Table_Cats.color: "gray",
            Table_Cats.description: "good cat",
            Table_Cats.breed: None
        }))
        
        await session.commit()
        
        print("-------------------------------\n\nAdd data \n\n ---------------------------------")
        
        
asyncio.run(start())