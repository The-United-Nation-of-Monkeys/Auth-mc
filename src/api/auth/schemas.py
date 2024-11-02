from pydantic import BaseModel, model_validator, EmailStr

from src.db.models.roles import Base_Roles
from src.api.responses import status_error_400

class Schema_Register(BaseModel):
    name: str
    login: EmailStr
    password: str
    role: str | None = None
    # group: str | None = None
    
    # @model_validator(mode="after")
    # @classmethod
    # def validate_group(cls, value):
    #     if cls.role == Base_Roles.student.value:
    #         if cls.group == None:
    #             return status_error_400("Student must have group")
    
    
class BearerTokenSchema(BaseModel):
    accessToken: str
    refreshToken: str
    
    
    
