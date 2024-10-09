from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
import uvicorn

from api.auth.auth import router as auth_router

from config import settings

app = FastAPI(
    title="cats", openapi_prefix="/api/v1/admin"
    )

@app.get("/")
def title():
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content="Auth mc")

app.include_router(auth_router)


def run():
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")

if __name__ == "__main__":
    run()