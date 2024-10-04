from httpx import AsyncClient

from src.config import settings

    
async def test_logout(ac: AsyncClient):
    response = await ac.get("/api/v1/admin/auth/logout")
    
    assert response.status_code == 200
    

async def test_auth_login(ac: AsyncClient):
    response = await ac.post("/api/v1/admin/auth/login", auth=("asd", "asd"))
    
    assert response.status_code == 200, "invalid password or username"
    
async def test_access(ac: AsyncClient):
    response = await ac.get("/api/v1/admin/auth/access")
    
    assert response.status_code == 200, "invalid token"
    
    
    
    
    