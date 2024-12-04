from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy import select
import uvicorn

from src.db.models.roles import Table_Roles
from src.db.configuration import async_session_factory
from src.api.auth.auth import router as auth_router
from src.api.confirmation.confirmation import router as confirmation_router
from src.config import settings
from src.broker.redis import redis
from src.api.account.account import router as account_router

app = FastAPI(
    title="Auth-mc", openapi_prefix="/api/v2"
    )

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def title():
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content="Auth mc")


for router in [confirmation_router, auth_router, account_router]:
    app.include_router(router)


def run():
    uvicorn.run(app, host="127.0.0.1", port=settings.server.port, log_level="info")

if __name__ == "__main__":
    run()
