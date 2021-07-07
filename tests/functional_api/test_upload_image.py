import os

import aiohttp
import pytest
from aiogqlc import GraphQLClient
from app.core.config import BASE_DIR

from .conftest import Client


@pytest.mark.asyncio
async def test_foo(client: Client) -> None:
    async with aiohttp.ClientSession() as session:
        filename = "README.md"
        variables = {"file": open(filename, "rb")}

        gql = GraphQLClient("http://127.0.0.1:8000/graphql/", session=session)

        response = await gql.execute(client.UPLOAD_USER_FILE, variables=variables)
        print(await response.json())

        with open(os.path.join(BASE_DIR, "app", "database", "file.txt")) as f:
            files = [f.readline() for _ in f]
        assert filename in files[-1]


def test_hello(client: Client) -> None:
    response = client.hello()

    assert "hello" in response.json().get("data")
