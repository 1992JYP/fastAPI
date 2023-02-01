import json
import pytest

from httpx import AsyncClient

@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/")
        assert response.status_code == 200
        assert response.json() == {"msg": "Hello World"}


@pytest.mark.asyncio
async def test_read_item():
    async with AsyncClient(base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/items/foo", params={"item_id": "1"})
        assert response.status_code == 200
        assert response.json() == {
            "id": "foo",
            "title": "Foo",
            "description": "There goes my hero",
        }


@pytest.mark.asyncio
async def test_create_item():
    async with AsyncClient(base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get(
            "/items/"
        )
        assert response.status_code == 200
        assert response.json() == "hello"