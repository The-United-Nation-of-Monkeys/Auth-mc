from pydantic import BaseModel, model_validator, EmailStr
from typing import Literal

from src.db.models.roles import Base_Roles
from src.api.responses import status_error_400

import enum

class Schema_Register(BaseModel):
    name: str
    login: EmailStr
    password: str
    role: str | None = None
    gender: Literal["male", "female"]

class BearerTokenSchema(BaseModel):
    accessToken: str
    refreshToken: str