import pytest

from config.end_points import EndPoint
from config.http_methods import HttpMethod
from utils.json_loader import load_json
from utils.booking_assertion_helper import BookingAssertion

def test_delete_booking(auth_token,client):
    id = 9
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={auth_token}"
    }

    response = client.request(
        method=HttpMethod.DELETE,
        endpoint=f"{EndPoint.DELETE_BOOKING}/{id}",
        headers=headers
    )

    assert response.status_code == 201
