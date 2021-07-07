from typing import Any, Optional, Union

from aiohttp import ClientResponse
from fastapi.testclient import TestClient
from requests import Response
from starlette.testclient import ASGI2App, ASGI3App


class Client(TestClient):
    UPLOAD_USER_FILE = """
    mutation($file: Upload!) {
        uploadUserImage(image: $file)
    }
    """

    HELLO = """
    query {
        hello
    }
    """

    def __init__(self, app: Union[ASGI2App, ASGI3App]) -> None:
        super().__init__(app)

    async def upload_user_file(self, variables: Optional[dict]) -> ClientResponse:
        ...

    def hello(self) -> Response:
        data = {"query": self.HELLO}

        return self._graphql(data)

    def _graphql(self, data: dict, files: Any = None) -> Response:
        return self.post("/graphql/", json=data, files=files)
