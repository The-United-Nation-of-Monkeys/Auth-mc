from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from sqlalchemy import select
import uvicorn

from src.db.models.roles import Table_Roles
from src.db.configuration import async_session_factory
from src.api.auth.auth import router as auth_router
from src.api.confirmation.confirmation import router as confirmation_router
from src.config import settings

app = FastAPI(
    title="Auth-mc", openapi_prefix="/api/v1"
    )

@app.get("/")
async def title():
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content="Auth mc")


for router in [confirmation_router, auth_router]:
    app.include_router(router)

def run():
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")

if __name__ == "__main__":
    run()
