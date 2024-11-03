from pydantic import BaseModel, model_validator, EmailStr

from src.db.models.roles import Base_Roles
from src.api.responses import status_error_400

class Schema_Register(BaseModel):
    name: str
    login: EmailStr
    password: str
    role: str | None = None

class BearerTokenSchema(BaseModel):
    accessToken: str
    refreshToken: str
    
    
    
