from pydantic import BaseModel, model_validator, EmailStr
from typing import Literal

from src.db.models.roles import Base_Roles
from src.api.responses import status_error_400

import enum

class SchemaRegister(BaseModel):
    name: str
    lastname: str
    patronymic: str
    login: EmailStr
    password: str
    role: str 
    gender: Literal["male", "female"]

class BearerTokenSchema(BaseModel):
    accessToken: str
    refreshToken: str