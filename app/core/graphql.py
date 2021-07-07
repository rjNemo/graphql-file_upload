from ariadne import make_executable_schema, snake_case_fallback_resolvers, upload_scalar
from ariadne.asgi import GraphQL
from fastapi import FastAPI

from ..schema import Mutation, Query, schema
from .config import DEBUG


def mount_graphql(app: FastAPI, path: str = "/graphql") -> FastAPI:
    app.mount(
        path,
        GraphQL(
            make_executable_schema(
                schema, Query, Mutation, snake_case_fallback_resolvers, upload_scalar
            ),
            debug=DEBUG,
        ),
    )

    return app
