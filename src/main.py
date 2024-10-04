from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from redis import asyncio as asyncredis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
import uvicorn

from api.auth.auth import router as auth_router
from api.cats.cats import router as cats_router
from config import settings

app = FastAPI(
    title="cats", openapi_prefix="/api/v1/admin"
    )

@app.get("/")
def title():
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content="Cats are good")

@app.on_event("startup")
async def startup_event():
    redis_cache = asyncredis.from_url(f"redis://{settings.redis.host}:{settings.redis.port}", 
                                      encoding = "utf8",
                                      decode_responses = True)
    FastAPICache.init(RedisBackend(redis_cache), prefix="fastapi-cache")


app.include_router(cats_router)
app.include_router(auth_router)


def run():
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")

if __name__ == "__main__":
    run()