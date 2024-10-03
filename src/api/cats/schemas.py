from pydantic import BaseModel


class Default_Cat_Schema(BaseModel):
    age: int
    color: str
    description: str
    breed: str | None = None