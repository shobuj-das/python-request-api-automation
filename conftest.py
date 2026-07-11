import pytest

from config.http_methods import HttpMethod
from config.api_client import ApiClient
from config.end_points import EndPoint

from utils.json_loader import load_json

@pytest.fixture(scope="session")
def client():
    return ApiClient()


@pytest.fixture(scope="session")
def auth_token(client):
    auth_payload = load_json("testdata/booking/auth_payload.json")

    response = client.request(
        method=HttpMethod.POST,
        endpoint=EndPoint.AUTH,
        payload=auth_payload
    )

    return response.json()["token"]
