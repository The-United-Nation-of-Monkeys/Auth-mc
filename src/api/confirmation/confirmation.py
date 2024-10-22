from fastapi import Depends, APIRouter

from api.responses import *
from api.confirmation.mail import *

router = APIRouter(
    prefix="/confirmation",
    tags=["Confirmation"]
)

class Confirmation:
    
    @router.get("/access")
    async def accessUser():
        Mail.sendConfirmationMessage()
        
        return status_success_200()