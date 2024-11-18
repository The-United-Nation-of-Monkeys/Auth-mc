from redis import ConnectionPool, Redis

from src.config import settings


class RedisClient:
    pool: ConnectionPool = ConnectionPool(host=settings.redis.host, port=settings.redis.port, db=0)

    def get_value(self, key: str):
        with Redis(connection_pool=self.pool) as redis:
            value = redis.get(key)
            return value
        
    def set_value(self, key: str, value: dict | str, expiration: int | None = None):
        with Redis(connection_pool=self.pool) as redis:
            if expiration:
                redis.set(key, value, expiration)
                return 
            
            redis.set(key, value)
            

redis = RedisClient()