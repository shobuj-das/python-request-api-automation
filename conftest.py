import pytest

from config.api_client import ApiClient

@pytest.fixture(scope="session")
def client():
    return ApiClient()
