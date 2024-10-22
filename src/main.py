from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from sqlalchemy import select
import uvicorn

from db.models.roles import Table_Roles
from db.configuration import async_session_factory
from api.auth.auth import router as auth_router
from api.confirmation.confirmation import router as confirmation_router

from config import settings

app = FastAPI(
    title="Auth-mc", openapi_prefix="/api/v1"
    )

@app.get("/")
async def title():
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content="Auth mc")

app.include_router(auth_router)
app.include_router(confirmation_router)

def run():
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")

if __name__ == "__main__":
    run()