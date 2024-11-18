from pydantic import BaseModel


class SSwitchPassword(BaseModel):
    new_password: str