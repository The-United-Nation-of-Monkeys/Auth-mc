from httpx import AsyncClient

from src.config import settings

async def test_error_auth_login_invalid_login(ac: AsyncClient):
    response = await ac.post("/api/v1/admin/auth/login", auth=("te", "test"))
    
    assert response.status_code == 401, "valid login"
    
async def test_error_auth_login_invalid_password(ac: AsyncClient):
    response = await ac.post("/api/v1/admin/auth/login", auth=("test", "te"))
    
    assert response.status_code == 401, "valid password"
    
async def test_error_access(ac: AsyncClient):
    response = await ac.get("/api/v1/admin/auth/access", cookies={settings.auth.type_token.refresh: ""})
    
    assert response.status_code == 401, "valid token"