from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from redis import asyncio as asyncredis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from src.api.auth.auth import router as auth_router
from src.api.cats.cats import router as cats_router
from src.config import settings

app = FastAPI(
    title="cats", openapi_prefix="/api/v1/admin"
    )

@app.get("/")
def title():
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content="not found")

@app.on_event("startup")
async def startup_event():
    redis_cache = asyncredis.from_url(f"redis://{settings.redis.host}:{settings.redis.port}", 
                                      encoding = "utf8",
                                      decode_responses = True)
    FastAPICache.init(RedisBackend(redis_cache), prefix="fastapi-cache")


app.include_router(cats_router)
app.include_router(auth_router)