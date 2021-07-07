import pytest
from ariadne import gql
from graphql import GraphQLSyntaxError

from ..schema import schema


def test_graphql_schema():
    try:
        gql(schema)
    except GraphQLSyntaxError:
        pytest.fail("GraphQL schema are invalid")
