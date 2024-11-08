from pathlib import Path
from pydantic import BaseModel
from celery import Celery
import datetime, os, dotenv

BASE_DIR = Path(__file__).parent.parent

dotenv.load_dotenv()

class DataBase(BaseModel):
    user: str = os.environ.get("DB_USER")
    name: str = os.environ.get("DB_NAME")
    host: str = os.environ.get("DB_HOST")
    port: str = os.environ.get("DB_PORT")
    password: str = os.environ.get("DB_PASSWORD")
    DATABASE_URL: str = f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{name}"
    
class TypeToken(BaseModel):
    refresh: str = "refresh"
    access: str = "access"
    
class Auth(BaseModel):
    public_key: Path = BASE_DIR / "src" / "certs" / "jwt-public.pem"
    private_key: Path = BASE_DIR / "src" / "certs" / "jwt-private.pem"
    algorithm: str = "RS256"
    access: datetime.timedelta = datetime.timedelta(minutes=15)
    refresh: datetime.timedelta = datetime.timedelta(hours=3)
    type_token: TypeToken = TypeToken()
    
# class Redis(BaseModel):
#     host: str = os.environ.get("REDIS_HOST")
#     port: str = os.environ.get("REDIS_PORT")
#     REDIS_URL: str = f"redis://{host}:{port}/0"
    
class Mail(BaseModel):
    mail: str = os.environ.get("MAIL")
    password: str = os.environ.get("MAIL_PASSWORD")
    
class Broker(BaseModel):
    host: str = os.environ.get("BROKER_HOST")
    port: str = os.environ.get("BROKER_PORT")
    BROKER_URL: str =  f"{host}:{port}"

class Server(BaseModel):
    host: str = os.environ.get("SERVER_HOST")
    port: str = os.environ.get("SERVER_PORT")
    protocol: str = os.environ.get("SERVER_PROTOCOL")
    SERVER_URL: str = f"{protocol}://{host}:{port}"

class Settings(BaseModel):
    database: DataBase = DataBase()
    auth: Auth = Auth()
    redis: Redis = Redis()
    mail: Mail = Mail()
    broker: Broker = Broker()
    server: Server = Server()


settings = Settings()
# celery_client = Celery('mc-auth', backend=settings.redis.REDIS_URL)
