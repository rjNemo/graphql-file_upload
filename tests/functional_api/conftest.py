import pytest
from app.main import app
from faker import Faker

from .client import Client


@pytest.fixture(scope="session")
def client() -> Client:
    return Client(app)


@pytest.fixture(scope="session")
def faker() -> Faker:
    faker = Faker()
    return faker
