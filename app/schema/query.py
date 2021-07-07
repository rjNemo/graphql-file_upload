from typing import Any

from ariadne import QueryType

Query = QueryType()


@Query.field("hello")
async def resolve_hello(*_: Any) -> str:
    return "Hello stranger"
