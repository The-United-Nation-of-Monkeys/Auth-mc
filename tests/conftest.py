from fastapi.testclient import TestClient
from typing import AsyncGenerator
from httpx import AsyncClient
import pytest, asyncio

from src.main import app


# client = TestClient(app)
base_client = AsyncClient(app=app, base_url="http://test")

@pytest.fixture(scope='session')
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac