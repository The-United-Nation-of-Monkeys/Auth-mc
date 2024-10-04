from httpx import AsyncClient
import pytest

from conftest import base_client
from src.config import settings
    
async def test_auth_login(ac: AsyncClient):
    response = await ac.post("/api/v1/admin/auth/login", auth=("test", "test"))
    
    assert response.status_code == 200, "no auth"
    
async def test_all_cats(ac: AsyncClient):
    response = await ac.get("/api/v1/admin/cats/all/cats")

    assert response.status_code == 200, "no auth"
    
async def test_all_breeds(ac: AsyncClient):
    response = await ac.get("/api/v1/admin/cats/cat/all/breeds")
    
    assert response.status_code == 200, "no auth"
    
async def test_filter_breed(ac: AsyncClient):
    response = await ac.get("api/v1/admin/cats/cat/all/breeds?breed='stating'")

    assert response.status_code == 200, "no auth"
    
async def test_cat_id(ac: AsyncClient):
    response = await ac.get("/api/v1/admin/cats/cat/1")
    
    assert response.status_code == 200, "no auth"
    
async def test_add_cat_no_breed(ac: AsyncClient):
    response = await ac.post("/api/v1/admin/cats/cat/add", json={
        "age": 12,
        "color": "black",
        "description": "good cat",
        "breed": None
    })
    
    assert response.status_code == 200, "no auth"
    
async def test_add_cat_no_breed(ac: AsyncClient):
    response = await ac.post("/api/v1/admin/cats/cat/add", json={
        "age": 12,
        "color": "black",
        "description": "good cat",
        "breed": "Siamese"
    })
    
    assert response.status_code == 200, "no auth"
    
async def test_update_cat(ac: AsyncClient):
    response = await ac.put("/api/v1/admin/cats/cat/update?id=1", json={
        "age": 13,
        "color": "wight",
        "description": "very good cat",
        "breed": "Maine Coon"
    })
    
    assert response.status_code == 200, "no auth"
    
async def test_delete_cat(ac: AsyncClient):
    response = await ac.delete("/api/v1/admin/cats/cat/del/1")
    response = await ac.delete("/api/v1/admin/cats/cat/del/2")
    response = await ac.delete("/api/v1/admin/cats/cat/del/3")
    
    
    assert response.status_code == 200, "no auth"
    

    

    
